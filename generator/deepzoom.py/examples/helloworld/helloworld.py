#!/usr/bin/env python
# -*- coding: utf-8 -*-

import deepzoom

# Specify your source image
SOURCE = "cells.png"

# Create Deep Zoom Image creator with weird parameters
creator = deepzoom.ImageCreator(tile_size=512, tile_overlap=0, tile_format="png",
                                image_quality=0.8, resize_filter="bicubic")

# Create Deep Zoom image pyramid from source
creator.create(SOURCE, "cells.dzi")
