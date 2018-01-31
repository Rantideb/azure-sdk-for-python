# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .build_trigger import BuildTrigger


class ImageTrigger(BuildTrigger):
    """A build trigger based on Image updates.

    :param type: Constant filled by server.
    :type type: str
    :param id: The unique identifier of a trigger.
    :type id: str
    :param image_name: Name of the repository or image.
    :type image_name: str
    :param tag: The tag name.
    :type tag: str
    """

    _validation = {
        'type': {'required': True},
        'id': {'required': True},
        'image_name': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'image_name': {'key': 'imageName', 'type': 'str'},
        'tag': {'key': 'tag', 'type': 'str'},
    }

    def __init__(self, id, image_name, tag=None):
        super(ImageTrigger, self).__init__()
        self.id = id
        self.image_name = image_name
        self.tag = tag
        self.type = 'ImageTrigger'
