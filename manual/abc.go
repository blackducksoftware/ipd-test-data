		kbResp, err := prodKbClient.SnippetMatchingComponentsWithResolvedLinks(content)
		utils.Die(err)
		logrus.Debugf("resp from snippet matching components %d chars:\n%s\n", len(content), json.MustMarshalToString(kbResp))

		bdResp, err := bdClient.SnippetMatchRaw(content)
		utils.Die(err)
		bdParsed, err := json.ParseString[map[string]interface{}](bdResp)
		utils.Die(err)
		logrus.Debugf("bd snippet match %d chars:\n%s\n\n\n", len(content), json.MustMarshalToString(bdParsed))

		kbToBd := NewBdSnippetMatchingResponse(kbResp)
		logrus.Debugf("kbToBd snippet match %d chars:\n%s\n\n\n", len(content), json.MustMarshalToString(kbToBd))


                kbResp, err := prodKbClient.SnippetMatchingComponentsWithResolvedLinks(content)
                utils.Die(err)
                logrus.Debugf("resp from snippet matching components %d chars:\n%s\n", len(content), json.MustMarshalToString(kbR\
esp))

                bdResp, err := bdClient.SnippetMatchRaw(content)
                utils.Die(err)
                bdParsed, err := json.ParseString[map[string]interface{}](bdResp)
                utils.Die(err)
                logrus.Debugf("bd snippet match %d chars:\n%s\n\n\n", len(content), json.MustMarshalToString(bdParsed))

                kbToBd := NewBdSnippetMatchingResponse(kbResp)
                logrus.Debugf("kbToBd snippet match %d chars:\n%s\n\n\n", len(content), json.MustMarshalToString(kbToBd))

