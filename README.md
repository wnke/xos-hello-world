# xos-hello-world

Implmentation of the helloWorld tuturial [basic-synchronizer](https://github.com/opencord/docs/blob/master/developer/tutorials/basic-synchronizer/intro.md) .

## XOS Synchronizer

XOS defines 3 types of steps (actions) that can be programed for each model:
1. [Sync step](https://github.com/opencord/xos/blob/5adc6e9e41ab38683e94858f755b0e58f01b1b21/docs/dev/sync_reference.md#sync-steps)
2. [Pull step](https://github.com/opencord/xos/blob/5adc6e9e41ab38683e94858f755b0e58f01b1b21/docs/dev/sync_reference.md#pull-steps)
3. [Event step](https://github.com/opencord/xos/blob/5adc6e9e41ab38683e94858f755b0e58f01b1b21/docs/dev/sync_reference.md#event-steps)

The first two steps are initiated by XOS targeting the micro-service being managed. Sync steps are triggers when the backind data model is changed and used to push configuration changes to the managed micro-service. Pull steps are triggered everytime the syncronizer event loop _loops_ and are use to retrive information from the managed micro-service.

The third step, Event step is trigered when an event is received via the message broker. The managed micro-service publishes some event to the messaga broker. This kind of step is assynchounous and can be triggered anytime depending of when the managed service publishes.






ADD to reload tosca


root@cord:~/xos-hello-world# curl -H "xos-username: admin@opencord.org" \
>     -H "xos-password: letmein" \
>     -X POST --data-binary @samples/hello-world.yaml \
>     http://localhost:30007/run


	ImportError: Import "custom_types/helloworldservice.yaml" is not valid.
	ImportError: Import "custom_types/helloworldserviceinstance.yaml" is not valid.
	InvalidTypeError: Type "tosca.nodes.HelloWorldServiceInstance" is not a valid type.
			InvalidTypeError(what=entitytype))
	UnknownFieldError: "properties" of template "serviceinstance" contains unknown field "hello_to". Refer to the definition to verify valid values.
	UnknownFieldError: "properties" of template "serviceinstance" contains unknown field "name". Refer to the definition to verify valid values.
	InvalidTypeError: Type "tosca.nodes.HelloWorldService" is not a valid type.
			InvalidTypeError(what=entitytype))
	UnknownFieldError: "properties" of template "service" contains unknown field "name". Refer to the definition to verify valid values.
	UnknownFieldError: "properties" of template "service" contains unknown field "hello_from". Refer to the definition to verify valid values.

