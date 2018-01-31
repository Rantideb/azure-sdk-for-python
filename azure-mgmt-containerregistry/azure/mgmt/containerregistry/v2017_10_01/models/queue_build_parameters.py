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

from msrest.serialization import Model


class QueueBuildParameters(Model):
    """The properties of a quick build.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: DockerBuildParameters

    :param type: Constant filled by server.
    :type type: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'Docker': 'DockerBuildParameters'}
    }

    def __init__(self):
        super(QueueBuildParameters, self).__init__()
        self.type = None
