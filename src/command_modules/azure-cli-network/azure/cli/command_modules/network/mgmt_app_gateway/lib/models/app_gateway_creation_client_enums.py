#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#---------------------------------------------------------------------------------------------
#pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class frontendType(Enum):

    public_ip = "publicIp"
    private_ip = "privateIp"


class httpListenerProtocol(Enum):

    http = "http"
    https = "https"


class httpSettingsCookieBasedAffinity(Enum):

    enabled = "enabled"
    disabled = "disabled"


class httpSettingsProtocol(Enum):

    http = "http"
    https = "https"


class privateIpAddressAllocation(Enum):

    dynamic = "dynamic"
    static = "static"


class publicIpAddressAllocation(Enum):

    dynamic = "dynamic"
    static = "static"


class publicIpType(Enum):

    none = "none"
    new = "new"
    existing_name = "existingName"
    existing_id = "existingId"


class routingRuleType(Enum):

    basic = "Basic"
    path_based_routing = "PathBasedRouting"


class subnetType(Enum):

    new = "new"
    existing_id = "existingId"
    existing_name = "existingName"


class DeploymentMode(Enum):

    incremental = "Incremental"
    complete = "Complete"