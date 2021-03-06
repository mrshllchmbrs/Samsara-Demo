# coding: utf-8

"""
    Samsara API

    # Introduction The Samsara REST API lets you interact with the Samsara Cloud from anything that can send an HTTP request. With the Samsara API you can build powerful applications and custom solutions with sensor data.  Samsara has endpoints available to track and analyze sensors, vehicles, and entire fleets. If you’re familiar with what you can build with a REST API, the following API reference guide will be your go-to resource.  API access to the Samsara cloud is available to all Samsara administrators. If you’d like to try the API, [contact us](https://www.samsara.com/free-trial). The API is currently in beta and may be subject to frequent changes.  # Connecting to the API There are two ways to connect to the API. If you prefer to use the API in Javascript or Python, we supply SDKs which you can download here: [Javascript SDK](https://github.com/samsarahq/samsara-js), [Python SDK](https://github.com/samsarahq/samsara-python).  If you’d rather use another language to interact with the Samsara API, the endpoints and examples are in the reference guide below.  

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VehicleMaintenancePassenger(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, check_engine_light=None, diagnostic_trouble_codes=None):
        """
        VehicleMaintenancePassenger - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'check_engine_light': 'VehicleMaintenancePassengerCheckEngineLight',
            'diagnostic_trouble_codes': 'list[VehicleMaintenancePassengerDiagnosticTroubleCodes]'
        }

        self.attribute_map = {
            'check_engine_light': 'checkEngineLight',
            'diagnostic_trouble_codes': 'diagnosticTroubleCodes'
        }

        self._check_engine_light = check_engine_light
        self._diagnostic_trouble_codes = diagnostic_trouble_codes

    @property
    def check_engine_light(self):
        """
        Gets the check_engine_light of this VehicleMaintenancePassenger.

        :return: The check_engine_light of this VehicleMaintenancePassenger.
        :rtype: VehicleMaintenancePassengerCheckEngineLight
        """
        return self._check_engine_light

    @check_engine_light.setter
    def check_engine_light(self, check_engine_light):
        """
        Sets the check_engine_light of this VehicleMaintenancePassenger.

        :param check_engine_light: The check_engine_light of this VehicleMaintenancePassenger.
        :type: VehicleMaintenancePassengerCheckEngineLight
        """

        self._check_engine_light = check_engine_light

    @property
    def diagnostic_trouble_codes(self):
        """
        Gets the diagnostic_trouble_codes of this VehicleMaintenancePassenger.
        Passenger vehicle DTCs.

        :return: The diagnostic_trouble_codes of this VehicleMaintenancePassenger.
        :rtype: list[VehicleMaintenancePassengerDiagnosticTroubleCodes]
        """
        return self._diagnostic_trouble_codes

    @diagnostic_trouble_codes.setter
    def diagnostic_trouble_codes(self, diagnostic_trouble_codes):
        """
        Sets the diagnostic_trouble_codes of this VehicleMaintenancePassenger.
        Passenger vehicle DTCs.

        :param diagnostic_trouble_codes: The diagnostic_trouble_codes of this VehicleMaintenancePassenger.
        :type: list[VehicleMaintenancePassengerDiagnosticTroubleCodes]
        """

        self._diagnostic_trouble_codes = diagnostic_trouble_codes

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, VehicleMaintenancePassenger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
