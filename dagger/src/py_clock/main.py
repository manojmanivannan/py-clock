import dagger
from dagger import dag, function, object_type


@object_type
class PyClock:
    @function
    def build_env(self, source: dagger.Directory, test: dagger.Directory) -> dagger.Container:
        """Build a ready-to-use development environment"""
        # create a Dagger cache volume for dependencies
        node_cache = dag.cache_volume("node")
        return (
            dag.container()
            # start from a base Node.js container
            .from_("python:3.11")
            .with_directory("/src/py_text_clock", source)
            .with_directory("/src/tests", test)
            .with_workdir("/src")
            .with_mounted_cache("/root/.cache/pip", dag.cache_volume("python-311"))
            .with_exec("pip install pytest click".split())
        )
    
    @function
    async def test(self, source: dagger.Directory, test: dagger.Directory) -> str:
        """Run tests"""
        return await (
            
            self.build_env(source, test)
            .with_exec(["echo", "Running tests..."])
            .with_exec(["pytest", "-s", "-v", "/src/tests"])
            .stdout()
        )
