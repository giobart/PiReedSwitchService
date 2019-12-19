

# Pi Reed Switch Service

This service pull data from a Reed Switch evey n seconds and make them available through the endpoint 
```/api/reedswitch/x ``` where x is the sensor number, just in case we have more than one sensor.

Is possible to set a notification endpoint that is called whenever the sensor changes the state. 
To setup a notification endpoint just update in the configuration the variable ``` NOTIFICATION_ENDPOINT ``` or set an environment variable in the container.

Is also possible to set an endpoint to turn on a light when the reed switch circuit is closed. 
The configuration of the endpoint can be found in the ``` LIGHT_ENDPOINT ```