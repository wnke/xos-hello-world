# xos-hello-world

Implmentation of the helloWorld tuturial [basic-synchronizer](https://github.com/opencord/docs/blob/master/developer/tutorials/basic-synchronizer/intro.md) .

## XOS Synchronizer Steps

XOS defines 3 types of steps (actions) that can be programed for each model:
1. [Sync step](./xos/synchronizer/steps/sync_hello_world_service.py) [More info](https://github.com/opencord/xos/blob/5adc6e9e41ab38683e94858f755b0e58f01b1b21/docs/dev/sync_reference.md#sync-steps)
2. [Pull step](./xos/synchronizer/pull_steps/pull_hello_world_service.py) [More info](https://github.com/opencord/xos/blob/5adc6e9e41ab38683e94858f755b0e58f01b1b21/docs/dev/sync_reference.md#pull-steps)
3. [Event step](./xos/synchronizer/event_steps/events_hello_world_service.py) [More info](https://github.com/opencord/xos/blob/5adc6e9e41ab38683e94858f755b0e58f01b1b21/docs/dev/sync_reference.md#event-steps)

The first two steps are initiated by XOS targeting the micro-service being managed. Sync steps are triggers when the backind data model is changed and used to push configuration changes to the managed micro-service. Pull steps are triggered everytime the syncronizer event loop _loops_ and are use to retrive information from the managed micro-service.

The third step, Event step is trigered when an event is received via the message broker. The managed micro-service publishes some event to the messaga broker. This kind of step is assynchounous and can be triggered anytime depending of when the managed service publishes.

## XOS Synchronizer Policies

XOS also defines (policies)[./xos/synchronizer/model_policies/policies_hello_world_service.py] as hooks for model events such as:
1. Create 
2. Update 
3. Delete 

[More info](https://github.com/opencord/xos/blob/5adc6e9e41ab38683e94858f755b0e58f01b1b21/docs/dev/sync_reference.md#model-policies)


## Notes
If you are having trouble uploading your tosca file, restart the tosca container:
```bash
kubectl delete $(kubectl get pods -o=name | grep tosca)
```