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


class Build(Model):
    """The properties for a build.

    :param build_id: The unique identifier for the build.
    :type build_id: str
    :param status: The current status of the build. Possible values include:
     'Queued', 'Started', 'Running', 'Succeeded', 'Failed', 'Cancelled'
    :type status: str or
     ~azure.mgmt.containerregistry.v2017_10_01.models.BuildStatus
    :param last_updated_time: The last updated time for the build.
    :type last_updated_time: datetime
    :param build_type: The type of build. Possible values include:
     'AutoBuild', 'QuickBuild'
    :type build_type: str or
     ~azure.mgmt.containerregistry.v2017_10_01.models.BuildType
    :param create_time: The time the build was created.
    :type create_time: datetime
    :param start_time: The time the build started.
    :type start_time: datetime
    :param finish_time: The time the build finished.
    :type finish_time: datetime
    :param output_images: The list of all images that were generated from the
     build.
    :type output_images:
     list[~azure.mgmt.containerregistry.v2017_10_01.models.ImageDescriptor]
    :param build_definition: All the properties of the build definition with
     which the build was started.
    :type build_definition: str
    :param trigger: The trigger that caused the build.
    :type trigger: str
    :param is_archive_enabled: The value that indicates whether archiving is
     enabled or not.
    :type is_archive_enabled: bool
    :param platform: The platform properties against which the build will
     happen.
    :type platform:
     ~azure.mgmt.containerregistry.v2017_10_01.models.PlatformProperties
    """

    _attribute_map = {
        'build_id': {'key': 'buildId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'last_updated_time': {'key': 'lastUpdatedTime', 'type': 'iso-8601'},
        'build_type': {'key': 'buildType', 'type': 'str'},
        'create_time': {'key': 'createTime', 'type': 'iso-8601'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'finish_time': {'key': 'finishTime', 'type': 'iso-8601'},
        'output_images': {'key': 'outputImages', 'type': '[ImageDescriptor]'},
        'build_definition': {'key': 'buildDefinition', 'type': 'str'},
        'trigger': {'key': 'trigger', 'type': 'str'},
        'is_archive_enabled': {'key': 'isArchiveEnabled', 'type': 'bool'},
        'platform': {'key': 'platform', 'type': 'PlatformProperties'},
    }

    def __init__(self, build_id=None, status=None, last_updated_time=None, build_type=None, create_time=None, start_time=None, finish_time=None, output_images=None, build_definition=None, trigger=None, is_archive_enabled=None, platform=None):
        super(Build, self).__init__()
        self.build_id = build_id
        self.status = status
        self.last_updated_time = last_updated_time
        self.build_type = build_type
        self.create_time = create_time
        self.start_time = start_time
        self.finish_time = finish_time
        self.output_images = output_images
        self.build_definition = build_definition
        self.trigger = trigger
        self.is_archive_enabled = is_archive_enabled
        self.platform = platform
