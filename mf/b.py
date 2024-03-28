/*
 * Copyright (C) 2020 Synopsys Inc.
 * http://www.synopsys.com/
 * All rights reserved.
 *
 * This software is the confidential and proprietary information of
 * Synopsys ("Confidential Information"). You shall not
 * disclose such Confidential Information and shall use it only in
 * accordance with the terms of the license agreement you entered into
 * with Synopsys.
 */

package com.blackducksoftware.core.rest.client;

import java.net.URI;
import java.util.Collections;
import java.util.List;
import java.util.Optional;

import org.apache.commons.lang3.StringUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestOperations;
import org.springframework.web.util.UriComponentsBuilder;
import org.springframework.web.util.UriTemplate;

import com.blackducksoftware.core.json.JsonPage;
import com.blackducksoftware.core.page.Page;
import com.blackducksoftware.core.page.ResourcePage;
import com.blackducksoftware.core.properties.api.Property;
import com.blackducksoftware.core.rest.exception.Rest404Exception;
import com.blackducksoftware.core.rest.exception.RestException;

/**
 * Rest resource client.
 * <p>
 * TODO: We should attempt to refactor this into a base class with a simple rest resource client and parameterized rest
 * resource client child classes to handle parameterization better.
 * <p>
 * TODO: Resolve how and if this is different from com.blackducksoftware.core.api.client.RestResourceClient
 */
public class RestResourceClient<T> {
    private final Logger logger = LoggerFactory.getLogger(getClass());

    private final String restEndPoint;

    private final RestOperations restTemplate;

    private final String singleFullPath;

    private final Class<T> clazz;

    public RestResourceClient(Property<String> scheme, Property<String> host, Property<Integer> port, Property<String> servicePath,
            Property<String> singleRelativePath, RestOperations restTemplate, Class<T> clazz) {
        this(scheme != null ? scheme.getValue() : null, host != null ? host.getValue() : null, port != null ? port.getValue() : -1,
                servicePath != null ? servicePath.getValue() : null, singleRelativePath != null ? singleRelativePath.getValue() : null,
                restTemplate, clazz);
    }

    public RestResourceClient(String scheme, String host, int port, String servicePath, String singleRelativePath, RestOperations restTemplate,
            Class<T> clazz) {
        this(UriComponentsBuilder.newInstance().scheme(scheme).host(host).port(port).path(servicePath).build().toUriString(), singleRelativePath, restTemplate,
                clazz);
    }

    public RestResourceClient(String restEndPoint, String singleRelativePath, RestOperations restTemplate, Class<T> clazz) {
        this.restEndPoint = restEndPoint;
        this.restTemplate = restTemplate;
        this.clazz = clazz;

        if (StringUtils.isBlank(singleRelativePath)) {
            this.singleFullPath = restEndPoint;
        } else {
            this.singleFullPath = restEndPoint + (singleRelativePath.startsWith("/") ? "" : "/") + singleRelativePath;
        }

        logger.debug("RestResourceClient created. SingleRelativePath = {}, URI = {} ", new Object[] { singleRelativePath, restEndPoint });
    }

    public RestResourceClient(URI uri, String singleRelativePath, RestOperations restTemplate, Class<T> clazz) {
        this(uri.toString(), singleRelativePath, restTemplate, clazz);
    }

    public void delete(RestResourcePathBuilder path, Object... uriVariables) {
        delete(getUrl(path), uriVariables);
    }

    public void deleteSingle(RestResourcePathBuilder path, Object... uriVariables) {
        delete(getUrl(path, singleFullPath), uriVariables);
    }

    public <S> S execute(RestResourcePathBuilder path, HttpMethod method, Object body, Class<S> returnClass, Object... uriVariables) {
        return executeUrl(getUrl(path), method, body, returnClass, uriVariables);
    }

    public T execute(RestResourcePathBuilder path, HttpMethod method, Object body, Object... uriVariables) {
        return execute(path, method, body, clazz, uriVariables);
    }

    public <S> S executeUrl(String url, HttpMethod method, Object body, Class<S> returnClass, Object... uriVariables) {
        HttpEntity<?> req = body == null ? null : new HttpEntity<>(body);
        ResponseEntity<S> response = exchange(url, method, req, returnClass, uriVariables);
        return response.getBody();
    }

    public <S> S executeUrl(String url, HttpMethod method, Object body, HttpHeaders headers, Class<S> returnClass, Object... uriVariables) {
        HttpEntity<?> req = (body != null || headers != null) ? new HttpEntity<>(body, headers) : null;
        ResponseEntity<S> response = exchange(url, method, req, returnClass, uriVariables);
        return response.getBody();
    }

    public T executeUrl(String url, HttpMethod method, Object body, Object... uriVariables) {
        return executeUrl(url, method, body, clazz, uriVariables);
    }

    public ResponseEntity<T> executeUrlAndReturnResponseEntity(RestResourcePathBuilder path, HttpMethod method, Object body,
            Object... uriVariables) {
        HttpEntity<?> req = body == null ? null : new HttpEntity<>(body);
        return exchange(getUrl(path), method, req, clazz, uriVariables);
    }

    public ResponseEntity<T> getResponseEntity(RestResourcePathBuilder path, Object... uriVariables) {
        try {
            return exchange(getUrl(path, singleFullPath), HttpMethod.GET, null, clazz, uriVariables);
        } catch (Rest404Exception e) {
            ResponseEntity<T> responseEntity = new ResponseEntity<>(HttpStatus.NOT_FOUND);
            return responseEntity;
        }
    }

    public <S> ResponseEntity<S> getResponseEntity(RestResourcePathBuilder path, Class<S> clazz, Object... uriVariables) {
        try {
            return exchange(getUrl(path), HttpMethod.GET, null, clazz, uriVariables);
        } catch (Rest404Exception e) {
            ResponseEntity<S> responseEntity = new ResponseEntity<>(HttpStatus.NOT_FOUND);
            return responseEntity;
        }
    }

    public String getAndReturnJson(RestResourcePathBuilder path, Object... uriVariables) {
        return getForObject(getUrl(path), String.class, uriVariables);
    }

    public <S> List<S> getList(RestResourcePathBuilder path, Class<S> returnClass, Object... uriVariables) {
        String json = getAndReturnJson(path, uriVariables);
        List<S> list = JsonPage.readList(json, returnClass);

        return list;
    }

    public List<T> getList(RestResourcePathBuilder path, Object... uriVariables) {
        return getList(path, clazz, uriVariables);
    }

    public List<T> getRequiredList(RestResourcePathBuilder path, Object... uriVariables) {
        try {
            return getList(path, clazz, uriVariables);
        } catch (Rest404Exception e) {
            return Collections.emptyList();
        }
    }

    public <S> Optional<S> getOptional(RestResourcePathBuilder path, Class<S> returnClass, Object... uriVariables) {
        try {
            S data = getSingle(path, returnClass, uriVariables);
            return Optional.of(data);
        } catch (Rest404Exception e) {
            return Optional.empty();
        }
    }

    public Optional<T> getOptional(RestResourcePathBuilder path, Object... uriVariables) {
        return getOptional(path, clazz, uriVariables);
    }

    public <S> Optional<S> getParameterizedOptional(RestResourcePathBuilder path, ParameterizedTypeReference<S> responseType, Object... uriVariables) {
        try {
            S data = getParameterizedSingle(path, responseType, uriVariables);
            return Optional.of(data);
        } catch (Rest404Exception e) {
            return Optional.empty();
        }
    }

    public <S> Page<S> getPage(RestResourcePathBuilder path, Class<S> returnClass, Object... uriVariables) {
        String json = getAndReturnJson(path, uriVariables);
        Page<S> page = JsonPage.readPage(json, returnClass);
        return page;
    }

    public Page<T> getPage(RestResourcePathBuilder path, Object... uriVariables) {
        return getPage(path, clazz, uriVariables);
    }

    public <S> ResourcePage<S> getResourcePage(RestResourcePathBuilder path, Class<S> returnClass, Object... uriVariables) {
        String json = getAndReturnJson(path, uriVariables);
        ResourcePage<S> page = JsonPage.readResourcePage(json, returnClass);
        return page;
    }

    public ResourcePage<T> getResourcePage(RestResourcePathBuilder path, Object... uriVariables) {
        return getResourcePage(path, clazz, uriVariables);
    }

    public String getRestEndPoint() {
        return restEndPoint;
    }

    public <S> S getSingle(RestResourcePathBuilder path, Class<S> returnClass, Object... uriVariables) {
        return getForObject(getUrl(path, singleFullPath), returnClass, uriVariables);
    }

    public <S> S getParameterizedSingle(RestResourcePathBuilder path, ParameterizedTypeReference<S> responseType, Object... uriVariables) {
        ResponseEntity<S> responseEntity = exchange(getUrl(path, singleFullPath), HttpMethod.GET, null, responseType, uriVariables);
        S body = responseEntity.getBody();
        return body;
    }

    public T getSingle(RestResourcePathBuilder path, Object... uriVariables) {
        return getSingle(path, clazz, uriVariables);
    }

    public String getSingleFullPath() {
        return this.singleFullPath;
    }

    public String getUrl(RestResourcePathBuilder path) {
        return getUrl(path, null);
    }

    private String getUrl(RestResourcePathBuilder path, String defaultFullPath) {
        logger.debug("path info : {}", path);

        String url;
        if (path == null) {
            url = StringUtils.isBlank(defaultFullPath) ? restEndPoint : defaultFullPath;
        } else {
            url = path.build(defaultFullPath, restEndPoint);
        }

        logger.info("url : {}", url);
        return url;
    }

    public <S> S post(RestResourcePathBuilder path, Object body, Class<S> returnClass, Object... uriVariables) {
        return executeUrl(getUrl(path), HttpMethod.POST, body, returnClass, uriVariables);
    }

    public T post(RestResourcePathBuilder path, Object body, Object... uriVariables) {
        return post(path, body, clazz, uriVariables);
    }

    // DO not need this method actually but just to test out changes
    public ResponseEntity<T> post(RestResourcePathBuilder path, String contentType, Object body) {
        HttpHeaders headers = new HttpHeaders();
        headers.add(HttpHeaders.CONTENT_TYPE, contentType);
        HttpEntity<?> requestEntity = new HttpEntity<>(body, headers);
        return exchange(getUrl(path), HttpMethod.POST, requestEntity, clazz);
    }

    public String postAndReturnJson(RestResourcePathBuilder path, Object body, Object... uriVariables) {
        try {
            return restTemplate.postForObject(getUrl(path), body, String.class, uriVariables);
        } catch (Rest404Exception e) { // NOPMD AvoidRethrowingException false positive
            throw e;
        } catch (RestException e) {
            log(getUrl(path), HttpMethod.POST, e, uriVariables);
            throw e;
        }
    }

    public <S> List<S> postList(RestResourcePathBuilder path, Class<S> returnClass, Object body, Object... uriVariables) {
        String json = postAndReturnJson(path, body, uriVariables);
        List<S> list = JsonPage.readList(json, returnClass);

        return list;
    }

    public List<T> postList(RestResourcePathBuilder path, Object body, Object... uriVariables) {
        return postList(path, clazz, body, uriVariables);
    }

    public void put(RestResourcePathBuilder path, Object body, Object... uriVariables) {
        try {
            restTemplate.put(getUrl(path), body, uriVariables);
        } catch (Rest404Exception e) { // NOPMD AvoidRethrowingException false positive
            throw e;
        } catch (RestException e) {
            log(getUrl(path), HttpMethod.PUT, e, uriVariables);
            throw e;
        }
    }

    public String putAndReturnJson(RestResourcePathBuilder path, Object body, Object... uriVariables) {
        return executeUrl(getUrl(path, singleFullPath), HttpMethod.PUT, body, String.class, uriVariables);
    }

    public <S> S putSingle(RestResourcePathBuilder path, Object body, Class<S> returnClass, Object... uriVariables) {
        return executeUrl(getUrl(path, singleFullPath), HttpMethod.PUT, body, returnClass, uriVariables);
    }

    public T putSingle(RestResourcePathBuilder path, Object body, Object... uriVariables) {
        return putSingle(path, body, clazz, uriVariables);
    }

    /**
     * all the complicated logging code here is because we want to log the url. the {@link RestResponseErrorHandler} can
     * not do that because it has no access to the url. this is typically called for all non-404 errors
     *
     */
    private void log(String url, HttpMethod method, RestException e, Object... uriVariables) {
        logger.warn("{} request for \"{}\" resulted in {} ({})",
                method.name(), new UriTemplate(url).expand(uriVariables), e.getHttpStatus().name(), e.getHttpStatus());
    }

    private <S> S getForObject(String url, Class<S> returnClass, Object... uriVariables) {
        try {
            return restTemplate.getForObject(url, returnClass, uriVariables);
        } catch (Rest404Exception e) { // NOPMD AvoidRethrowingException false positive
            throw e;
        } catch (RestException e) {
            log(url, HttpMethod.GET, e, uriVariables);
            throw e;
        }
    }

    private <S> ResponseEntity<S> exchange(String url, HttpMethod method, HttpEntity<?> requestEntity, ParameterizedTypeReference<S> responseType,
            Object... uriVariables) {
        try {
            return restTemplate.exchange(url, method, requestEntity, responseType, uriVariables);
        } catch (Rest404Exception e) { // NOPMD AvoidRethrowingException false positive
            throw e;
        } catch (RestException e) {
            log(url, method, e, uriVariables);
            throw e;
        }
    }

    private <S> ResponseEntity<S> exchange(String url, HttpMethod method, HttpEntity<?> requestEntity, Class<S> responseType, Object... uriVariables) {
        try {
            return restTemplate.exchange(url, method, requestEntity, responseType, uriVariables);
        } catch (Rest404Exception e) { // NOPMD AvoidRethrowingException false positive
            throw e;
        } catch (RestException e) {
            log(url, method, e, uriVariables);
            throw e;
        }
    }

    private void delete(String url, Object... uriVariables) {
        try {
            restTemplate.delete(url, uriVariables);
        } catch (Rest404Exception e) { // NOPMD AvoidRethrowingException false positive
            throw e;
        } catch (RestException e) {
            log(url, HttpMethod.DELETE, e, uriVariables);
            throw e;
        }
    }
}
