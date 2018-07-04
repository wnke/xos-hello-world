# xos-hello-world

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

