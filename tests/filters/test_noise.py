#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/thumbor/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com thumbor@googlegroups.com


import unittest

from preggy import expect

from tests.base import FilterTestCase


@unittest.skip("Does not work in CI - Comparison of image failing in Ubuntu")
class NoiseFilterTestCase(FilterTestCase):
    def test_noise_filter(self):
        image = self.get_filtered('source.jpg', 'thumbor.filters.noise', 'noise(200,123)')
        expected = self.get_fixture('noise.jpg')

        ssim = self.get_ssim(image, expected)
        expect(ssim).to_be_greater_than(0.98)
