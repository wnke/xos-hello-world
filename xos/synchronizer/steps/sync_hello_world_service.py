from synchronizers.new_base.SyncInstanceUsingAnsible import SyncStep, DeferredException 
from synchronizers.new_base.modelaccessor import HelloWorldServiceInstance 

from xosconfig import Config
from multistructlog import create_logger

log = create_logger(Config().get('logging'))


class SyncHelloWorldServiceInstance(SyncStep):
    provides = [HelloWorldServiceInstance]

    observes = HelloWorldServiceInstance

    def sync_record(self, o):
        log.debug("HelloWorldServiceInstance has been updated!", object=str(o), hello_to=o.hello_to)
        if o.hello_to == "Tyrion Lannister":
          raise DeferredException("Maybe later")
        if o.hello_to == "Joffrey Baratheon":
          raise Exception("Maybe not")

        log.info("%s is saying hello to %s" % (o.owner.leaf_model.hello_from, o.hello_to))

    def delete_record(self, o):
        log.debug("HelloWorldServiceInstance has been deleted!", object=str(o), hello_to=o.hello_to)

