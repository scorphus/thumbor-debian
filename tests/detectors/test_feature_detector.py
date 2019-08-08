#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/thumbor/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com thumbor@googlegroups.com

from os.path import abspath

from preggy import expect
from tests.base import DetectorTestCase

from thumbor.detectors.feature_detector import Detector as FeatureDetector


class FeatureDetectorTestCase(DetectorTestCase):

    def test_should_detect_multiple_points(self):
        with open(abspath('./tests/fixtures/images/no_face.jpg')) as f:
            self.engine.load(f.read(), None)

        FeatureDetector(self.context, 0, None).detect(lambda: None)
        detection_result = self.context.request.focal_points
        expect(len(detection_result)).to_be_greater_than(1)
        expect(detection_result[0].origin).to_equal('alignment')

    def test_should_detect_a_single_point(self):
        with open(abspath('./tests/fixtures/images/single_point.jpg')) as f:
            self.engine.load(f.read(), None)

        FeatureDetector(self.context, 0, None).detect(lambda: None)
        detection_result = self.context.request.focal_points
        expect(len(detection_result)).to_equal(1)
        expect(detection_result[0].origin).to_equal('alignment')

    def test_should_not_detect_points(self):
        with open(abspath('./tests/fixtures/images/1x1.png')) as f:
            self.engine.load(f.read(), None)

        FeatureDetector(self.context, 0, []).detect(lambda: None)
        detection_result = self.context.request.focal_points
        expect(detection_result).to_length(0)
