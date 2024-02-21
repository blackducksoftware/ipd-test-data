package utils

import (
	"github.com/pkg/errors"
	"github.com/sirupsen/logrus"
)

func SetUpLogger(logLevelStr string) error {
	logLevel, err := logrus.ParseLevel(logLevelStr)
	if err != nil {
		return errors.Wrapf(err, "unable to parse the specified log level: '%s'", logLevel)
	}
	logrus.SetLevel(logLevel)
	logrus.SetFormatter(&logrus.TextFormatter{
		FullTimestamp: true,
	})
	logrus.Infof("log level set to '%s'", logrus.GetLevel())
	return nil
}

func GetSomething() {
	// TODO
}

func GetSomethingElse() {
	// TODO
}

func GetSomething3() {
	// TODO
}

func GetSomething4() {
	// TODO
}

func GetSomething5() {
	// TODO
}
