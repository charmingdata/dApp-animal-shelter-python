import { ethers } from "https://cdn-cors.ethers.io/lib/ethers-5.7.2.esm.min.js";

const CONTRACT_ADDRESS = "0xc6BbCfcC9aFf07D657B78F39b4A56330db375cC6";



const CONTRACT_ABI = [
  {
    inputs: [],
    stateMutability: "nonpayable",
    type: "constructor",
  },
  {
    inputs: [],
    name: "NotShelterOwner",
    type: "error",
  },
  {
    inputs: [],
    name: "PetIdAlreadyTaken",
    type: "error",
  },
  {
    inputs: [],
    name: "SheleterDeleted",
    type: "error",
  },
  {
    inputs: [],
    name: "ShelterNotAvaliable",
    type: "error",
  },
  {
    anonymous: false,
    inputs: [
      {
        indexed: false,
        internalType: "uint256",
        name: "shelterId",
        type: "uint256",
      },
      {
        indexed: true,
        internalType: "enum ShelterDB.Country",
        name: "shelterCountry",
        type: "uint8",
      },
      {
        indexed: true,
        internalType: "bool",
        name: "atCapacity",
        type: "bool",
      },
      {
        indexed: true,
        internalType: "bool",
        name: "isDeleted",
        type: "bool",
      },
    ],
    name: "ShelterInfo",
    type: "event",
  },
  {
    inputs: [
      {
        internalType: "uint256",
        name: "",
        type: "uint256",
      },
    ],
    name: "ShelterListings",
    outputs: [
      {
        internalType: "string",
        name: "shelterName",
        type: "string",
      },
      {
        internalType: "enum ShelterDB.Country",
        name: "shelterCountry",
        type: "uint8",
      },
      {
        internalType: "string",
        name: "shelterCity",
        type: "string",
      },
      {
        internalType: "string",
        name: "shelterZipCode",
        type: "string",
      },
      {
        internalType: "bool",
        name: "atCapacity",
        type: "bool",
      },
      {
        internalType: "address",
        name: "shelterOwner",
        type: "address",
      },
      {
        internalType: "bool",
        name: "isDeleted",
        type: "bool",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [
      {
        internalType: "uint256",
        name: "_shelterId",
        type: "uint256",
      },
      {
        internalType: "string",
        name: "_name",
        type: "string",
      },
      {
        internalType: "string",
        name: "_petType",
        type: "string",
      },
      {
        internalType: "string",
        name: "_size",
        type: "string",
      },
      {
        internalType: "string",
        name: "_sex",
        type: "string",
      },
      {
        internalType: "string",
        name: "_age",
        type: "string",
      },
      {
        internalType: "uint256",
        name: "_petId",
        type: "uint256",
      },
    ],
    name: "addPet",
    outputs: [],
    stateMutability: "nonpayable",
    type: "function",
  },
  {
    inputs: [
      {
        internalType: "string",
        name: "_shelterName",
        type: "string",
      },
      {
        internalType: "enum ShelterDB.Country",
        name: "_shelterCountry",
        type: "uint8",
      },
      {
        internalType: "string",
        name: "_shelterCity",
        type: "string",
      },
      {
        internalType: "string",
        name: "_shelterZipCode",
        type: "string",
      },
    ],
    name: "addShelter",
    outputs: [],
    stateMutability: "nonpayable",
    type: "function",
  },
  {
    inputs: [
      {
        internalType: "uint256",
        name: "_shelterId",
        type: "uint256",
      },
    ],
    name: "getShelterListing",
    outputs: [
      {
        components: [
          {
            internalType: "string",
            name: "shelterName",
            type: "string",
          },
          {
            internalType: "enum ShelterDB.Country",
            name: "shelterCountry",
            type: "uint8",
          },
          {
            internalType: "string",
            name: "shelterCity",
            type: "string",
          },
          {
            internalType: "string",
            name: "shelterZipCode",
            type: "string",
          },
          {
            internalType: "bool",
            name: "atCapacity",
            type: "bool",
          },
          {
            internalType: "address",
            name: "shelterOwner",
            type: "address",
          },
          {
            internalType: "bool",
            name: "isDeleted",
            type: "bool",
          },
        ],
        internalType: "struct ShelterDB.Shelter",
        name: "",
        type: "tuple",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [
      {
        internalType: "uint256",
        name: "_shelterId",
        type: "uint256",
      },
    ],
    name: "getShelterPets",
    outputs: [
      {
        components: [
          {
            internalType: "string",
            name: "name",
            type: "string",
          },
          {
            internalType: "string",
            name: "petType",
            type: "string",
          },
          {
            internalType: "string",
            name: "size",
            type: "string",
          },
          {
            internalType: "string",
            name: "sex",
            type: "string",
          },
          {
            internalType: "string",
            name: "age",
            type: "string",
          },
          {
            internalType: "uint256",
            name: "petId",
            type: "uint256",
          },
        ],
        internalType: "struct ShelterDB.Pet[]",
        name: "",
        type: "tuple[]",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [],
    name: "totalPets",
    outputs: [
      {
        internalType: "uint256",
        name: "",
        type: "uint256",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [],
    name: "totalShelterId",
    outputs: [
      {
        internalType: "uint256",
        name: "",
        type: "uint256",
      },
    ],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [
      {
        internalType: "uint256",
        name: "_shelterId",
        type: "uint256",
      },
      {
        internalType: "string",
        name: "_shelterName",
        type: "string",
      },
      {
        internalType: "enum ShelterDB.Country",
        name: "_shelterCountry",
        type: "uint8",
      },
      {
        internalType: "string",
        name: "_shelterCity",
        type: "string",
      },
      {
        internalType: "string",
        name: "_shelterZipCode",
        type: "string",
      },
      {
        internalType: "bool",
        name: "_newCapacity",
        type: "bool",
      },
      {
        internalType: "bool",
        name: "_isDeleted",
        type: "bool",
      },
    ],
    name: "updateShelter",
    outputs: [],
    stateMutability: "nonpayable",
    type: "function",
  },
];

// targets sepolia chain:   https://chainlist.org/?search=sepolia&testnets=true
const targetNetworkId = "0xaa36a7";
// const targetNetworkId = "0x5a2"; // zkEVM testnet

// checks if current chain matches with the one we need
const checkNetwork = async () => {
  if (window.ethereum) {
    const currentChainId = await window.ethereum.request({
      method: "eth_chainId",
    });

    // return true if network id is the same
    if (currentChainId == targetNetworkId) {
      console.log("true");
      return true;
    }
    // return false if network id is different and switch network
    console.log("false");

    await window.ethereum.request({
      method: "wallet_switchEthereumChain",
      params: [{ chainId: targetNetworkId }],
    });
    window.location.reload();
  }
};
window.checkNetwork = checkNetwork;

const provider = new ethers.providers.Web3Provider(window.ethereum);
await provider.send("eth_requestAccounts", []);
const signer = provider.getSigner();
const contract = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, signer);

async function addingShelters(v_shelter, v_country, v_city, v_zipcode) {
  // create transaction
  const unsignedTrx = await contract.populateTransaction.addShelter(
    v_shelter,
    v_country,
    v_city,
    v_zipcode
  );

  console.log("Transaction created");
  const txResponse = await signer.sendTransaction(unsignedTrx);
  console.log(`Transaction signed and sent: ${txResponse.hash}`);
  await txResponse.wait();

  // get the block number where this transaction was mined
  const txReceipt = await provider.getTransactionReceipt(txResponse.hash);
  console.log(`Transaction was mined in block: ${txReceipt.blockNumber}`);
  const blocknum = txReceipt.blockNumber;

  // get the ShelterInfo event emitted by the contract in this blocknumber
  const event = await contract.queryFilter("ShelterInfo", blocknum, blocknum);
  console.log(event);

  console.log(
    `Transaction has been mined. You can view it here: https://sepolia.etherscan.io/tx/${txResponse.hash}`
  );
  try {
    // extract the shelter id from the event
    const extractShelterId = event[0].args.shelterId.toNumber();
    return extractShelterId;
  } catch (error) {
    console.log(error);
  }
}
// expose the transaction to the clientside callback
window.addingShelters = addingShelters;

async function updateMyShelter(
  id,
  v_name,
  country,
  city,
  zip,
  capacity,
  deleted
) {
  // create transaction
  console.log("before unsignedTrx");
  console.log(capacity);
  const unsignedTrx = await contract.populateTransaction.updateShelter(
    id,
    v_name,
    country,
    city,
    zip,
    capacity,
    deleted
  );
  console.log("created unsigned transaction");

  // send transaction via signer so it's automatically signed
  const txResponse = await signer.sendTransaction(unsignedTrx);
  await txResponse.wait(2);
  try {
    console.log(`Transaction signed and sent: ${txResponse.hash}`);
  } catch (error) {
    console.log(error);
  }
  // wait for block
  // await txResponse.wait(2);

  console.log("Contract Hash:", txResponse.hash);
  window.alert("Successfully updated shelter!");
}
// expose the transaction to the clientside callback
window.updateMyShelter = updateMyShelter;
