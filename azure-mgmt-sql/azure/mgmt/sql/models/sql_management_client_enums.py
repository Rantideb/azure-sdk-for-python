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

from enum import Enum


class BackupLongTermRetentionPolicyState(Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class RestorePointType(Enum):

    discrete = "DISCRETE"
    continuous = "CONTINUOUS"


class CapabilityStatus(Enum):

    visible = "Visible"
    available = "Available"
    default = "Default"
    disabled = "Disabled"


class MaxSizeUnits(Enum):

    megabytes = "Megabytes"
    gigabytes = "Gigabytes"
    terabytes = "Terabytes"
    petabytes = "Petabytes"


class PerformanceLevelUnit(Enum):

    dtu = "DTU"


class CheckNameAvailabilityReason(Enum):

    invalid = "Invalid"
    already_exists = "AlreadyExists"


class ServerConnectionType(Enum):

    default = "Default"
    proxy = "Proxy"
    redirect = "Redirect"


class CreateMode(Enum):

    copy = "Copy"
    default = "Default"
    non_readable_secondary = "NonReadableSecondary"
    online_secondary = "OnlineSecondary"
    point_in_time_restore = "PointInTimeRestore"
    recovery = "Recovery"
    restore = "Restore"
    restore_long_term_retention_backup = "RestoreLongTermRetentionBackup"


class DatabaseEdition(Enum):

    web = "Web"
    business = "Business"
    basic = "Basic"
    standard = "Standard"
    premium = "Premium"
    premium_rs = "PremiumRS"
    free = "Free"
    stretch = "Stretch"
    data_warehouse = "DataWarehouse"
    system = "System"
    system2 = "System2"


class ServiceObjectiveName(Enum):

    system = "System"
    system0 = "System0"
    system1 = "System1"
    system2 = "System2"
    system3 = "System3"
    system4 = "System4"
    system2_l = "System2L"
    system3_l = "System3L"
    system4_l = "System4L"
    free = "Free"
    basic = "Basic"
    s0 = "S0"
    s1 = "S1"
    s2 = "S2"
    s3 = "S3"
    s4 = "S4"
    s6 = "S6"
    s7 = "S7"
    s9 = "S9"
    s12 = "S12"
    p1 = "P1"
    p2 = "P2"
    p3 = "P3"
    p4 = "P4"
    p6 = "P6"
    p11 = "P11"
    p15 = "P15"
    prs1 = "PRS1"
    prs2 = "PRS2"
    prs4 = "PRS4"
    prs6 = "PRS6"
    dw100 = "DW100"
    dw200 = "DW200"
    dw300 = "DW300"
    dw400 = "DW400"
    dw500 = "DW500"
    dw600 = "DW600"
    dw1000 = "DW1000"
    dw1200 = "DW1200"
    dw1000c = "DW1000c"
    dw1500 = "DW1500"
    dw1500c = "DW1500c"
    dw2000 = "DW2000"
    dw2000c = "DW2000c"
    dw3000 = "DW3000"
    dw2500c = "DW2500c"
    dw3000c = "DW3000c"
    dw6000 = "DW6000"
    dw5000c = "DW5000c"
    dw6000c = "DW6000c"
    dw7500c = "DW7500c"
    dw10000c = "DW10000c"
    dw15000c = "DW15000c"
    dw30000c = "DW30000c"
    ds100 = "DS100"
    ds200 = "DS200"
    ds300 = "DS300"
    ds400 = "DS400"
    ds500 = "DS500"
    ds600 = "DS600"
    ds1000 = "DS1000"
    ds1200 = "DS1200"
    ds1500 = "DS1500"
    ds2000 = "DS2000"
    elastic_pool = "ElasticPool"


class TransparentDataEncryptionStatus(Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class RecommendedIndexAction(Enum):

    create = "Create"
    drop = "Drop"
    rebuild = "Rebuild"


class RecommendedIndexState(Enum):

    active = "Active"
    pending = "Pending"
    executing = "Executing"
    verifying = "Verifying"
    pending_revert = "Pending Revert"
    reverting = "Reverting"
    reverted = "Reverted"
    ignored = "Ignored"
    expired = "Expired"
    blocked = "Blocked"
    success = "Success"


class RecommendedIndexType(Enum):

    clustered = "CLUSTERED"
    nonclustered = "NONCLUSTERED"
    columnstore = "COLUMNSTORE"
    clusteredcolumnstore = "CLUSTERED COLUMNSTORE"


class ReadScale(Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class SampleName(Enum):

    adventure_works_lt = "AdventureWorksLT"


class TransparentDataEncryptionActivityStatus(Enum):

    encrypting = "Encrypting"
    decrypting = "Decrypting"


class ElasticPoolEdition(Enum):

    basic = "Basic"
    standard = "Standard"
    premium = "Premium"


class SecurityAlertPolicyState(Enum):

    new = "New"
    enabled = "Enabled"
    disabled = "Disabled"


class SecurityAlertPolicyEmailAccountAdmins(Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class SecurityAlertPolicyUseServerDefault(Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class DataMaskingState(Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class DataMaskingRuleState(Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class DataMaskingFunction(Enum):

    default = "Default"
    ccn = "CCN"
    email = "Email"
    number = "Number"
    ssn = "SSN"
    text = "Text"


class ElasticPoolState(Enum):

    creating = "Creating"
    ready = "Ready"
    disabled = "Disabled"


class GeoBackupPolicyState(Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class StorageKeyType(Enum):

    storage_access_key = "StorageAccessKey"
    shared_access_key = "SharedAccessKey"


class AuthenticationType(Enum):

    sql = "SQL"
    ad_password = "ADPassword"


class UnitType(Enum):

    count = "count"
    bytes = "bytes"
    seconds = "seconds"
    percent = "percent"
    count_per_second = "countPerSecond"
    bytes_per_second = "bytesPerSecond"


class PrimaryAggregationType(Enum):

    none = "None"
    average = "Average"
    count = "Count"
    minimum = "Minimum"
    maximum = "Maximum"
    total = "Total"


class UnitDefinitionType(Enum):

    count = "Count"
    bytes = "Bytes"
    seconds = "Seconds"
    percent = "Percent"
    count_per_second = "CountPerSecond"
    bytes_per_second = "BytesPerSecond"


class ReplicationRole(Enum):

    primary = "Primary"
    secondary = "Secondary"
    non_readable_secondary = "NonReadableSecondary"
    source = "Source"
    copy = "Copy"


class ReplicationState(Enum):

    pending = "PENDING"
    seeding = "SEEDING"
    catch_up = "CATCH_UP"
    suspended = "SUSPENDED"


class BlobAuditingPolicyState(Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class ServerKeyType(Enum):

    service_managed = "ServiceManaged"
    azure_key_vault = "AzureKeyVault"


class ReadWriteEndpointFailoverPolicy(Enum):

    manual = "Manual"
    automatic = "Automatic"


class ReadOnlyEndpointFailoverPolicy(Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class FailoverGroupReplicationRole(Enum):

    primary = "Primary"
    secondary = "Secondary"


class OperationOrigin(Enum):

    user = "user"
    system = "system"


class IdentityType(Enum):

    system_assigned = "SystemAssigned"


class SyncAgentState(Enum):

    online = "Online"
    offline = "Offline"
    never_connected = "NeverConnected"


class SyncMemberDbType(Enum):

    azure_sql_database = "AzureSqlDatabase"
    sql_server_database = "SqlServerDatabase"


class SyncGroupLogType(Enum):

    all = "All"
    error = "Error"
    warning = "Warning"
    success = "Success"


class SyncConflictResolutionPolicy(Enum):

    hub_win = "HubWin"
    member_win = "MemberWin"


class SyncGroupState(Enum):

    not_ready = "NotReady"
    error = "Error"
    warning = "Warning"
    progressing = "Progressing"
    good = "Good"


class SyncDirection(Enum):

    bidirectional = "Bidirectional"
    one_way_member_to_hub = "OneWayMemberToHub"
    one_way_hub_to_member = "OneWayHubToMember"


class SyncMemberState(Enum):

    sync_in_progress = "SyncInProgress"
    sync_succeeded = "SyncSucceeded"
    sync_failed = "SyncFailed"
    disabled_tombstone_cleanup = "DisabledTombstoneCleanup"
    disabled_backup_restore = "DisabledBackupRestore"
    sync_succeeded_with_warnings = "SyncSucceededWithWarnings"
    sync_cancelling = "SyncCancelling"
    sync_cancelled = "SyncCancelled"
    un_provisioned = "UnProvisioned"
    provisioning = "Provisioning"
    provisioned = "Provisioned"
    provision_failed = "ProvisionFailed"
    de_provisioning = "DeProvisioning"
    de_provisioned = "DeProvisioned"
    de_provision_failed = "DeProvisionFailed"
    reprovisioning = "Reprovisioning"
    reprovision_failed = "ReprovisionFailed"
    un_reprovisioned = "UnReprovisioned"


class VirtualNetworkRuleState(Enum):

    initializing = "Initializing"
    in_progress = "InProgress"
    ready = "Ready"
    deleting = "Deleting"
    unknown = "Unknown"


class ManagementOperationState(Enum):

    pending = "Pending"
    in_progress = "InProgress"
    succeeded = "Succeeded"
    failed = "Failed"
    cancel_in_progress = "CancelInProgress"
    cancelled = "Cancelled"
