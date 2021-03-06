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


class TemperatureResponseSensors(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, ambient_temperature=None, probe_temperature=None):
        """
        TemperatureResponseSensors - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'ambient_temperature': 'int',
            'probe_temperature': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'ambient_temperature': 'ambientTemperature',
            'probe_temperature': 'probeTemperature'
        }

        self._id = id
        self._ambient_temperature = ambient_temperature
        self._probe_temperature = probe_temperature

    @property
    def id(self):
        """
        Gets the id of this TemperatureResponseSensors.
        ID of the sensor.

        :return: The id of this TemperatureResponseSensors.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TemperatureResponseSensors.
        ID of the sensor.

        :param id: The id of this TemperatureResponseSensors.
        :type: int
        """

        self._id = id

    @property
    def ambient_temperature(self):
        """
        Gets the ambient_temperature of this TemperatureResponseSensors.
        Currently reported ambient temperature in millidegrees celsius.

        :return: The ambient_temperature of this TemperatureResponseSensors.
        :rtype: int
        """
        return self._ambient_temperature

    @ambient_temperature.setter
    def ambient_temperature(self, ambient_temperature):
        """
        Sets the ambient_temperature of this TemperatureResponseSensors.
        Currently reported ambient temperature in millidegrees celsius.

        :param ambient_temperature: The ambient_temperature of this TemperatureResponseSensors.
        :type: int
        """

        self._ambient_temperature = ambient_temperature

    @property
    def probe_temperature(self):
        """
        Gets the probe_temperature of this TemperatureResponseSensors.
        Currently reported probe temperature in millidegrees celsius. If no probe is connected, this parameter will not be reported.

        :return: The probe_temperature of this TemperatureResponseSensors.
        :rtype: int
        """
        return self._probe_temperature

    @probe_temperature.setter
    def probe_temperature(self, probe_temperature):
        """
        Sets the probe_temperature of this TemperatureResponseSensors.
        Currently reported probe temperature in millidegrees celsius. If no probe is connected, this parameter will not be reported.

        :param probe_temperature: The probe_temperature of this TemperatureResponseSensors.
        :type: int
        """

        self._probe_temperature = probe_temperature

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
        if not isinstance(other, TemperatureResponseSensors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
