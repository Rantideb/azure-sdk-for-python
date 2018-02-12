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

from .service_update_properties import ServiceUpdateProperties


class StatefulServiceUpdateProperties(ServiceUpdateProperties):
    """The properties of a stateful service resource for patch operations.

    :param placement_constraints: The placement constraints as a string.
     Placement constraints are boolean expressions on node properties and allow
     for restricting a service to particular nodes based on the service
     requirements. For example, to place a service on nodes where NodeType is
     blue specify the following: "NodeColor == blue)".
    :type placement_constraints: str
    :param correlation_scheme:
    :type correlation_scheme:
     list[~azure.mgmt.servicefabric.models.ServiceCorrelationDescription]
    :param service_load_metrics:
    :type service_load_metrics:
     list[~azure.mgmt.servicefabric.models.ServiceLoadMetricDescription]
    :param service_placement_policies:
    :type service_placement_policies:
     list[~azure.mgmt.servicefabric.models.ServicePlacementPolicyDescription]
    :param default_move_cost: Possible values include: 'Zero', 'Low',
     'Medium', 'High'
    :type default_move_cost: str or ~azure.mgmt.servicefabric.models.enum
    :param service_kind: Constant filled by server.
    :type service_kind: str
    :param target_replica_set_size: The target replica set size as a number.
    :type target_replica_set_size: int
    :param min_replica_set_size: The minimum replica set size as a number.
    :type min_replica_set_size: int
    :param replica_restart_wait_duration: The duration between when a replica
     goes down and when a new replica is created, represented in ISO 8601
     format (hh:mm:ss.s).
    :type replica_restart_wait_duration: datetime
    :param quorum_loss_wait_duration: The maximum duration for which a
     partition is allowed to be in a state of quorum loss, represented in ISO
     8601 format (hh:mm:ss.s).
    :type quorum_loss_wait_duration: datetime
    :param stand_by_replica_keep_duration: The definition on how long StandBy
     replicas should be maintained before being removed, represented in ISO
     8601 format (hh:mm:ss.s).
    :type stand_by_replica_keep_duration: datetime
    """

    _validation = {
        'service_kind': {'required': True},
        'target_replica_set_size': {'minimum': 1},
        'min_replica_set_size': {'minimum': 1},
    }

    _attribute_map = {
        'placement_constraints': {'key': 'placementConstraints', 'type': 'str'},
        'correlation_scheme': {'key': 'correlationScheme', 'type': '[ServiceCorrelationDescription]'},
        'service_load_metrics': {'key': 'serviceLoadMetrics', 'type': '[ServiceLoadMetricDescription]'},
        'service_placement_policies': {'key': 'servicePlacementPolicies', 'type': '[ServicePlacementPolicyDescription]'},
        'default_move_cost': {'key': 'defaultMoveCost', 'type': 'str'},
        'service_kind': {'key': 'serviceKind', 'type': 'str'},
        'target_replica_set_size': {'key': 'targetReplicaSetSize', 'type': 'int'},
        'min_replica_set_size': {'key': 'minReplicaSetSize', 'type': 'int'},
        'replica_restart_wait_duration': {'key': 'replicaRestartWaitDuration', 'type': 'iso-8601'},
        'quorum_loss_wait_duration': {'key': 'quorumLossWaitDuration', 'type': 'iso-8601'},
        'stand_by_replica_keep_duration': {'key': 'standByReplicaKeepDuration', 'type': 'iso-8601'},
    }

    def __init__(self, placement_constraints=None, correlation_scheme=None, service_load_metrics=None, service_placement_policies=None, default_move_cost=None, target_replica_set_size=None, min_replica_set_size=None, replica_restart_wait_duration=None, quorum_loss_wait_duration=None, stand_by_replica_keep_duration=None):
        super(StatefulServiceUpdateProperties, self).__init__(placement_constraints=placement_constraints, correlation_scheme=correlation_scheme, service_load_metrics=service_load_metrics, service_placement_policies=service_placement_policies, default_move_cost=default_move_cost)
        self.target_replica_set_size = target_replica_set_size
        self.min_replica_set_size = min_replica_set_size
        self.replica_restart_wait_duration = replica_restart_wait_duration
        self.quorum_loss_wait_duration = quorum_loss_wait_duration
        self.stand_by_replica_keep_duration = stand_by_replica_keep_duration
        self.service_kind = 'Stateful'