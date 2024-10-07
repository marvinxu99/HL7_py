from flask import Flask, jsonify
import asyncio
from fhirpy import AsyncFHIRClient

app = Flask(__name__)

async def fetch_patients():
    # Create an instance of the async FHIR client
    client = AsyncFHIRClient(
        'https://fhir.simplifier.net/mxfhir',
        None,
        {
            'Accept': 'application/fhir+json'
        }
    )
    # Search for patients
    resources = client.resources('Patient')  # Return lazy search set
    resources = resources.search(name='Marvin').limit(10).sort('name')
    patients = await resources.fetch()  # Returns list of AsyncFHIRResource

    return [pt.serialize() for pt in patients]


async def fetch_encounters():
    # Create an instance of the async FHIR client
    client = AsyncFHIRClient(
        'https://fhir.simplifier.net/mxfhir',
        None,
        {
            'Accept': 'application/fhir+json'
        }
    )
    # Search for patients
    resources = client.resources('Encounter')  # Return lazy search set
    resources = resources.search(name='Marvin').limit(10).sort('name')
    encounters = await resources.fetch()  # Returns list of AsyncFHIRResource

    return [enc.serialize() for enc in encounters]


@app.route('/patients', methods=['GET'])
def get_patients():
    # Use asyncio.run to execute the async function within a synchronous route
    patients = asyncio.run(fetch_patients())
    return jsonify(patients)

@app.route('/encounters', methods=['GET'])
def get_encoiunters():
    # Use asyncio.run to execute the async function within a synchronous route
    patients = asyncio.run(fetch_encounters())
    return jsonify(patients)

if __name__ == '__main__':
    app.run(debug=True)
