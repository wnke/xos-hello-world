from xosconfig import Config
from multistructlog import create_logger
from synchronizers.new_base.pullstep import PullStep
from synchronizers.new_base.modelaccessor import HelloWorldServiceInstance

log = create_logger(Config().get('logging'))


class HelloWorldServiceInstancePullStep(PullStep):
    def __init__(self):
        super(HelloWorldServiceInstancePullStep, self).__init__(observed_model=HelloWorldServiceInstance)

    def pull_records(self):
        log.info("pulling HelloWorldServiceInstance")

        if HelloWorldServiceInstance.objects.filter(name="Pulled Record", hello_to="Dude"):
            log.info("Nothing new to pull!")
            return

        # create an empty model
        o = HelloWorldServiceInstance()
        # code to fetch information
        # populate the model
        o.hello_to = "Dude"
        o.name = "Pulled Record"
        o.no_sync = True # this is required to prevent the synchronizer to be invoked and start a loop
        log.info("Pulled one record!")
        o.save()
