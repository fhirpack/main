import pytest as pt
from conftest import drillUnconnected
import tests as ts
import fhirdrill as fd

# this is an example fixture with session scope,
# only for the fhirdrill package, with autouse enabled and a finalizer
# this fixture can be used by any test under src/fhirdrill


@pt.fixture(scope="session", autouse=True)
def packageSessionFixture(request):
    ts.debug("fhirdrill session confSetup")

    def packageSessionFixtureFin():
        ts.debug("fhirdrill session confTeardown")
        pass

    request.addfinalizer(packageSessionFixtureFin)


# uncomment to use start the test FHIR server in docker and  build your frame
# @pt.fixture(scope="session")
# def patientFrame(drillDocker):
#     f = drillDocker.getPatients(["1","181","525","821"])

# uncomment to use .env to connect to the configured FHIR server and  build your frame
# @pt.fixture(scope="session")
# def patientFrame(drillEnv):
#     f = drillEnv.getPatients(["1","181","525","821"])

# uncomment to use files in /tests/data to build your frame
@pt.fixture(scope="session")
def patientFrame(drillUnconnected):
    f = drillUnconnected.getFromFiles(
        [f"{ts.TEST_DATA_DIR}/fhirdrill.extraction.base.getFromFiles.patients.00.in"]
    )
    result = f
    return result


@pt.fixture(scope="session")
def patientResourceList(patientFrame):
    p = patientFrame.data.values
    return p


# uncomment to use start the test FHIR server in docker and  build your frame
# def observationFrame(drillDocker):
#     f = drillDocker.getObservations(["9","10","11","12"])

# uncomment to use .env to connect to the configured FHIR server and  build your frame
# def observationFrame(drillEnv):
#     f = drillEnv.getObservations(["9","10","11","12"])

# uncomment to use files in /tests/data to build your frame
@pt.fixture(scope="session")
def observationFrame(drillUnconnected):
    f = drillUnconnected.getFromFiles(
        [f"{ts.TEST_DATA_DIR}/fhirdrill.observations.00.in"]
    )
    result = f
    return result


@pt.fixture(scope="session")
def observationResourceList(observationFrame):
    o = observationFrame.data.values
    result = o
    return result


@pt.fixture(scope="session")
def patientReferenceList(patientResourceList):
    r = [e.to_reference() for e in patientResourceList]
    result = r
    return result


@pt.fixture(scope="session")
def patientResource(patientResourceList):
    p = patientResourceList[0]
    return p


@pt.fixture(scope="session")
def patientReference(patientReferenceList):
    r = patientReferenceList[0]
    result = r
    return result


@pt.fixture(scope="session")
def patientAsDict(patientResourceList):
    p = patientResourceList[0].serialize()
    return p
