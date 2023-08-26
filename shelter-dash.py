from dash import (
    Dash,
    html,
    callback,
    clientside_callback,
    Output,
    Input,
    State,
    no_update,
)
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
import pandas as pd
from web3 import Web3
import dash_mantine_components as dmc
import json

component = dmc.MantineProvider(withGlobalStyles=True, theme={"colorScheme": "dark"})
with open("contract-abi.json", "r") as infile:
    abi = json.load(infile)


# abi_data = """[
# 	{
# 		"inputs": [],
# 		"stateMutability": "nonpayable",
# 		"type": "constructor"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "NotShelterOwner",
# 		"type": "error"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "PetIdAlreadyTaken",
# 		"type": "error"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "SheleterDeleted",
# 		"type": "error"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "ShelterNotAvaliable",
# 		"type": "error"
# 	},
# 	{
# 		"anonymous": false,
# 		"inputs": [
# 			{
# 				"indexed": false,
# 				"internalType": "uint256",
# 				"name": "shelterId",
# 				"type": "uint256"
# 			},
# 			{
# 				"indexed": true,
# 				"internalType": "enum ShelterDB.Country",
# 				"name": "shelterCountry",
# 				"type": "uint8"
# 			},
# 			{
# 				"indexed": true,
# 				"internalType": "bool",
# 				"name": "atCapacity",
# 				"type": "bool"
# 			},
# 			{
# 				"indexed": true,
# 				"internalType": "bool",
# 				"name": "isDeleted",
# 				"type": "bool"
# 			}
# 		],
# 		"name": "ShelterInfo",
# 		"type": "event"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "",
# 				"type": "uint256"
# 			}
# 		],
# 		"name": "ShelterListings",
# 		"outputs": [
# 			{
# 				"internalType": "string",
# 				"name": "shelterName",
# 				"type": "string"
# 			},
# 			{
# 				"internalType": "enum ShelterDB.Country",
# 				"name": "shelterCountry",
# 				"type": "uint8"
# 			},
# 			{
# 				"internalType": "string",
# 				"name": "shelterCity",
# 				"type": "string"
# 			},
# 			{
# 				"internalType": "string",
# 				"name": "shelterZipCode",
# 				"type": "string"
# 			},
# 			{
# 				"internalType": "bool",
# 				"name": "atCapacity",
# 				"type": "bool"
# 			},
# 			{
# 				"internalType": "address",
# 				"name": "shelterOwner",
# 				"type": "address"
# 			},
# 			{
# 				"internalType": "bool",
# 				"name": "isDeleted",
# 				"type": "bool"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "_shelterId",
# 				"type": "uint256"
# 			},
# 			{
# 				"internalType": "string",
# 				"name": "_name",
# 				"type": "string"
# 			},
# 			{
# 				"internalType": "string",
# 				"name": "_petType",
# 				"type": "string"
# 			},
# 			{
# 				"internalType": "string",
# 				"name": "_size",
# 				"type": "string"
# 			},
# 			{
# 				"internalType": "string",
# 				"name": "_sex",
# 				"type": "string"
# 			},
# 			{
# 				"internalType": "string",
# 				"name": "_age",
# 				"type": "string"
# 			},
# 			{
# 				"internalType": "uint256",
# 				"name": "_petId",
# 				"type": "uint256"
# 			}
# 		],
# 		"name": "addPet",
# 		"outputs": [],
# 		"stateMutability": "nonpayable",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "string",
# 				"name": "_shelterName",
# 				"type": "string"
# 			},
# 			{
# 				"internalType": "enum ShelterDB.Country",
# 				"name": "_shelterCountry",
# 				"type": "uint8"
# 			},
# 			{
# 				"internalType": "string",
# 				"name": "_shelterCity",
# 				"type": "string"
# 			},
# 			{
# 				"internalType": "string",
# 				"name": "_shelterZipCode",
# 				"type": "string"
# 			}
# 		],
# 		"name": "addShelter",
# 		"outputs": [],
# 		"stateMutability": "nonpayable",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "_shelterId",
# 				"type": "uint256"
# 			}
# 		],
# 		"name": "getShelterListing",
# 		"outputs": [
# 			{
# 				"components": [
# 					{
# 						"internalType": "string",
# 						"name": "shelterName",
# 						"type": "string"
# 					},
# 					{
# 						"internalType": "enum ShelterDB.Country",
# 						"name": "shelterCountry",
# 						"type": "uint8"
# 					},
# 					{
# 						"internalType": "string",
# 						"name": "shelterCity",
# 						"type": "string"
# 					},
# 					{
# 						"internalType": "string",
# 						"name": "shelterZipCode",
# 						"type": "string"
# 					},
# 					{
# 						"internalType": "bool",
# 						"name": "atCapacity",
# 						"type": "bool"
# 					},
# 					{
# 						"internalType": "address",
# 						"name": "shelterOwner",
# 						"type": "address"
# 					},
# 					{
# 						"internalType": "bool",
# 						"name": "isDeleted",
# 						"type": "bool"
# 					}
# 				],
# 				"internalType": "struct ShelterDB.Shelter",
# 				"name": "",
# 				"type": "tuple"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "_shelterId",
# 				"type": "uint256"
# 			}
# 		],
# 		"name": "getShelterPets",
# 		"outputs": [
# 			{
# 				"components": [
# 					{
# 						"internalType": "string",
# 						"name": "name",
# 						"type": "string"
# 					},
# 					{
# 						"internalType": "string",
# 						"name": "petType",
# 						"type": "string"
# 					},
# 					{
# 						"internalType": "string",
# 						"name": "size",
# 						"type": "string"
# 					},
# 					{
# 						"internalType": "string",
# 						"name": "sex",
# 						"type": "string"
# 					},
# 					{
# 						"internalType": "string",
# 						"name": "age",
# 						"type": "string"
# 					},
# 					{
# 						"internalType": "uint256",
# 						"name": "petId",
# 						"type": "uint256"
# 					}
# 				],
# 				"internalType": "struct ShelterDB.Pet[]",
# 				"name": "",
# 				"type": "tuple[]"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "totalPets",
# 		"outputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "",
# 				"type": "uint256"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "totalShelterId",
# 		"outputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "",
# 				"type": "uint256"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "_shelterId",
# 				"type": "uint256"
# 			},
# 			{
# 				"internalType": "string",
# 				"name": "_shelterName",
# 				"type": "string"
# 			},
# 			{
# 				"internalType": "enum ShelterDB.Country",
# 				"name": "_shelterCountry",
# 				"type": "uint8"
# 			},
# 			{
# 				"internalType": "string",
# 				"name": "_shelterCity",
# 				"type": "string"
# 			},
# 			{
# 				"internalType": "string",
# 				"name": "_shelterZipCode",
# 				"type": "string"
# 			},
# 			{
# 				"internalType": "bool",
# 				"name": "_newCapacity",
# 				"type": "bool"
# 			},
# 			{
# 				"internalType": "bool",
# 				"name": "_isDeleted",
# 				"type": "bool"
# 			}
# 		],
# 		"name": "updateShelter",
# 		"outputs": [],
# 		"stateMutability": "nonpayable",
# 		"type": "function"
# 	}
# ]"""
# abi = json.loads(abi_data)


app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.CYBORG],
    external_scripts=[{"src": "../static/signerinfo.js", "type": "module"}],
)
app.layout = dbc.Container(
    [
        html.H1("Welcome to the Animal Shelter dApp!", style={"textAlign": "center"}),
        html.H5(
            "A contract that keeps track of animal shelters capacity.",
            style={"textAlign": "center"},
        ),
        dbc.Alert(
            children="",
            id="tx-alert",
            is_open=False,
            duration=5000,
            style={"width": "50%"},
        ),
        html.H3("Add New Shelter"),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Label("Name:"),
                        dbc.Input(
                            id="insert-shelter",
                            required=True,
                            type="text",
                            value="Insert Shelter Name...",
                            style={"width": 200},
                        ),
                    ],
                    width=6,
                    lg=3,
                ),
                dbc.Col(
                    [
                        html.Label("Country:"),
                        dbc.RadioItems(
                            options=[
                                {"label": "USA", "value": 0},
                                {"label": "India", "value": 1},
                                {"label": "Brazil", "value": 2},
                            ],
                            value=0,
                            id="insert-country",
                            inline=True,
                        ),
                    ],
                    width=6,
                    lg=3,
                ),
                dbc.Col(
                    [
                        html.Label("City:"),
                        dbc.Input(
                            id="insert-city",
                            required=True,
                            type="text",
                            value="Insert Shelter City...",
                            style={"width": 200},
                        ),
                    ],
                    width=6,
                    lg=3,
                ),
                dbc.Col(
                    [
                        html.Label("Zip Code:"),
                        dbc.Input(
                            id="insert-zipcode",
                            required=True,
                            type="text",
                            value="Insert Shelter Zip Code...",
                            style={"width": 200},
                        ),
                    ],
                    width=6,
                    lg=3,
                ),
            ],
            className="mb-2",
        ),
        html.Div(
            style={"width": 200},
            children=[
                dmc.LoadingOverlay(
                    dmc.Stack(
                        id="loading-form",
                        children=[
                            dbc.Button(
                                "Submit",
                                id="submit-btn",
                                color="primary",
                                n_clicks=0,
                                className="my-4",
                            ),
                        ],
                    ),
                    overlayColor="black",
                ),
            ],
        ),
        html.H3("Update your Shelter Information"),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Label("Name:"),
                        dbc.Input(
                            id="insert-name2",
                            required=True,
                            type="text",
                            value="Insert Shelter Name...",
                            style={"width": 200},
                        ),
                    ],
                    width=6,
                    lg=3,
                ),
                dbc.Col(
                    [
                        html.Label("Country:"),
                        dbc.RadioItems(
                            options=[
                                {"label": "USA", "value": 0},
                                {"label": "India", "value": 1},
                                {"label": "Brazil", "value": 2},
                            ],
                            value=0,
                            id="insert-country2",
                            inline=True,
                        ),
                    ],
                    width=6,
                    lg=3,
                ),
                dbc.Col(
                    [
                        html.Label("City:"),
                        dbc.Input(
                            id="insert-city2",
                            required=True,
                            type="text",
                            value="Insert Shelter City...",
                            style={"width": 200},
                        ),
                    ],
                    width=6,
                    lg=3,
                ),
                dbc.Col(
                    [
                        html.Label("Zip Code:"),
                        dbc.Input(
                            id="insert-zipcode2",
                            required=True,
                            type="text",
                            value="Insert Shelter Zip Code...",
                            style={"width": 200},
                        ),
                    ],
                    width=6,
                    lg=3,
                ),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Label("Shelter ID:"),
                        dbc.Input(
                            id="insert-shelterID2",
                            placeholder="Type your shelter id...",
                            type="number",
                            min=0,
                            required=True,
                            value=1,
                            style={"width": 200},
                        ),
                    ],
                    width=6,
                    lg=3,
                ),
                dbc.Col(
                    [
                        html.Label("Shelter at Capacity?"),
                        dbc.RadioItems(
                            id="select-capacity2",
                            options=[
                                {"label": "True", "value": True},
                                {"label": "False", "value": False},
                            ],
                            value=False,
                            inline=True,
                            style={"width": 200},
                        ),
                    ],
                    width=6,
                    lg=3,
                ),
                dbc.Col(
                    [
                        html.Label("Delete Shelter?"),
                        dbc.RadioItems(
                            id="delete-shelter2",
                            options=[
                                {"label": "True", "value": True},
                                {"label": "False", "value": False},
                            ],
                            value=False,
                            inline=True,
                            style={"width": 200},
                        ),
                    ],
                    width=6,
                    lg=3,
                ),
            ]
        ),
        html.Div(
            style={"width": 200},
            children=[
                dmc.LoadingOverlay(
                    dmc.Stack(
                        id="loading-form2",
                        children=[
                            dbc.Button(
                                "Submit",
                                id="update-shelter-btn2",
                                color="primary",
                                n_clicks=0,
                                className="my-4",
                            ),
                        ],
                    ),
                    overlayColor="black",
                ),
            ],
        ),
        html.H3("Get Shelter Information"),
        html.Label("Shelter ID:"),
        html.Div(
            style={"width": 200},
            children=[
                dmc.LoadingOverlay(
                    dmc.Stack(
                        id="loading-form3",
                        children=[
                            dbc.Input(
                                id="single-shelterID",
                                placeholder="Insert shelter id...",
                                type="number",
                                min=0,
                                required=True,
                                value=0,
                                style={"width": 200},
                            ),
                            dbc.Button(
                                "Submit",
                                id="shelter-btn",
                                color="primary",
                                n_clicks=0,
                                className="mb-4",
                                style={"width": 200},
                            ),
                        ],
                    ),
                    overlayColor="black",
                )
            ],
        ),
        html.Div(id="shelter-data-placeholder", style={"whiteSpace": "pre-wrap"}),
        html.H3("Get shelters with capacity to receive animals"),
        dbc.Button(
            "Submit",
            id="shelter-btn4",
            color="primary",
            n_clicks=0,
            className="mb-4",
            style={"width": 200},
        ),
        html.Div(id="shelter-data-placeholder2"),
    ]
)

# Add New shelter
clientside_callback(
    """async function (n, v_shelter, v_country, v_city, v_zipcode) {
         try { await checkNetwork();
         } catch (e) {console.log(e)}
         try {
         getShelterId = await addingShelters(v_shelter, v_country, v_city, v_zipcode);
         } catch (e) { return [window.dash_clientside.no_update, false, ""]; }
         return [window.dash_clientside.no_update, true,`Success! Make sure to save your shelter ID: ${getShelterId}`] 
       }
    """,
    Output("loading-form", "children"),
    Output("tx-alert", "is_open"),
    Output("tx-alert", "children"),
    Input("submit-btn", "n_clicks"),
    State("insert-shelter", "value"),
    State("insert-country", "value"),
    State("insert-city", "value"),
    State("insert-zipcode", "value"),
    prevent_initial_call=True,
)


# Update Shelter Information
clientside_callback(
    """async function (n, id, v_name, country, city, zip, capacity, deleted) {
         try { await checkNetwork();
         } catch (e) {console.log(e)}
         try {
         await updateMyShelter(id, v_name, country, city, zip, capacity, deleted);
         } catch (e) { return window.dash_clientside.no_update; }
         return window.dash_clientside.no_update
       }
    """,
    Output("loading-form2", "children"),
    Input("update-shelter-btn2", "n_clicks"),
    State("insert-shelterID2", "value"),
    State("insert-name2", "value"),
    State("insert-country2", "value"),
    State("insert-city2", "value"),
    State("insert-zipcode2", "value"),
    State("select-capacity2", "value"),
    State("delete-shelter2", "value"),
    prevent_initial_call=True,
)


# Get Shelter Information by ID
@callback(
    Output("shelter-data-placeholder", "children"),
    Output("loading-form3", "children"),
    Input("shelter-btn", "n_clicks"),
    State("single-shelterID", "value"),
    prevent_initial_call=True,
)
def access_shelter_data(_, value):
    # Connect to a node:  zkEVM_rpc = "https://rpc.public.zkevm-test.net"
    sepolia_rpc = "https://skilled-magical-wave.ethereum-sepolia.discover.quiknode.pro/8e62ba67d81c7d8a28bab69034da8cc5d9f04bea/"
    w3 = Web3(Web3.HTTPProvider(sepolia_rpc))

    # Create an instance of the smart contract
    address = w3.to_checksum_address("0xc6BbCfcC9aFf07D657B78F39b4A56330db375cC6")
    contract = w3.eth.contract(address=address, abi=abi)
    try:
        (
            name,
            country,
            city,
            zipcode,
            at_capacity,
            owner,
            deleted,
        ) = contract.functions.getShelterListing(value).call()

        result = (
            f"Name: {name},",
            f"Country: {country}, ",
            f"City: {city}, ",
            f"Zipcode: {zipcode} ",
            f"At Capacity: {at_capacity} ",
            f"Owner: {owner} ",
            f"Deleted: {deleted} ",
        )
        result = "\n".join(result)

    except Exception as e:
        result = "Shelter ID does not exist or has been deleted!"

    return result, no_update


# Get all shelters with capacity
@callback(
    Output("shelter-data-placeholder2", "children"),
    Input("shelter-btn4", "n_clicks"),
    prevent_initial_call=True,
)
def access_shelter_data(_):
    sepolia_rpc = "https://skilled-magical-wave.ethereum-sepolia.discover.quiknode.pro/8e62ba67d81c7d8a28bab69034da8cc5d9f04bea/"
    w3 = Web3(Web3.HTTPProvider(sepolia_rpc))
    address = w3.to_checksum_address("0xc6BbCfcC9aFf07D657B78F39b4A56330db375cC6")
    contract = w3.eth.contract(address=address, abi=abi)
    # Get all ShelterInfo events. Attention that block range queries are limited by quicknode to around 10,000 blocks:
    # https://support.quicknode.com/hc/en-us/articles/10258449939473-Understanding-the-10-000-Block-Range-Limit-for-querying-Logs-and-Events
    # A possible solution is to save the block number in an external database after each event is triggered in the smart contract;
    # then, query the blockchain logs (...ShelterInfo.get_logs() only for those blocks. In other words, instead of querying 10,000 blocks on the
    # blockchain, just query the blocks that have been saved in the external database.

    # block_numbers_from_external_database = [4141567, 4141783, 4135944, 4141589, 4141360]
    # latestShelterEvents = {}
    # for block_number in block_numbers_from_external_database:
    #     block_event = contract.events.ShelterInfo.get_logs(
    #         fromBlock=block_number,
    #         toBlock=block_number,
    #     )
    #
    #     theShelterId = block_event[0]["args"]["shelterId"]
    # 	# Mapping to track the latest event data (blocknumber) for each shelter in case there are duplicate events of the same shelter.
    #     if (
    #         theShelterId not in latestShelterEvents
    #         or block_event[0]["blockNumber"]
    #         > latestShelterEvents[theShelterId]["blockNumber"]
    #     ):
    #         latestShelterEvents[theShelterId] = {
    #             "id": theShelterId,
    #             "blockNumber": block_event[0]["blockNumber"],
    #         }
    #     print(latestShelterEvents[theShelterId]["blockNumber"])
    # print("-----------------------------------------------All Unique Shelters:")
    # print(latestShelterEvents)
    # shelters_with_capacity = []
    # # continue code here from line 823.

    events = contract.events.ShelterInfo.get_logs(
        fromBlock=4135936,
        toBlock=4145030,
    )

    # Mapping to track the latest event data for each shelter in case there are duplicate events of the same shelter.
    # Duplicate events are likely to happen because an event is triggered in the smart contract if a shelter is entered or updated
    latestShelterEvents = {}
    for shelter in events:
        theShelterId = shelter["args"]["shelterId"]
        if (
            theShelterId not in latestShelterEvents
            or shelter["blockNumber"] > latestShelterEvents[theShelterId]["blockNumber"]
        ):
            latestShelterEvents[theShelterId] = {
                "id": theShelterId,
                "blockNumber": shelter["blockNumber"],
            }
    print("-----------------------------------------------All Unique Shelters:")
    print(latestShelterEvents)

    # Get all shelters where atCapacity is false by
    # triggering the shelterListings solidity mapping function to extract the complete shelter struct by shelterID
    shelters_with_capacity = []
    for idOfShelter in latestShelterEvents:
        s = contract.functions.getShelterListing(idOfShelter).call()
        keys = ["name", "country", "city", "zipcode", "at_capacity", "owner", "deleted"]
        shelter_data = {keys[i]: value for i, value in enumerate(s)}

        if shelter_data["at_capacity"] == False:
            shelters_with_capacity.append(shelter_data)
    print("-----------------------------------------------Shelters with capacity:")
    print(shelters_with_capacity)

    df = pd.DataFrame(
        list(shelters_with_capacity),
        columns=[
            "name",
            "country",
            "city",
            "zipcode",
            "at_capacity",
            "owner",
            "deleted",
        ],
    )

    # df = df.drop("owner", axis=1)
    grid = dag.AgGrid(
        id="our-table",
        className="ag-theme-alpine-dark",
        rowData=df.to_dict("records"),
        columnDefs=[{"field": i} for i in df.columns],
    )

    return grid


if __name__ == "__main__":
    app.run(debug=True)
