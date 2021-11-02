# Cool-Sheep-Club-NFT

https://opensea.io/collection/cool-sheep-club

This repository has everything you need to make your own polygon ERC721 nfts.
You will need python with the Pillow and Selenium librairies, node.js and firefox with the metamask extension.

## NFT Generation
- Run the "Generation.py" python script to create the images and a txt file with the NFT prices based on their rarity. (Generation the images is slow, it took me more than 20 minutes to generate 10000 images)
- You have to host the images on the platform of you choice (I use [Pinata](https://www.pinata.cloud/)), the link needs to end with the number of the NFT or you need to change the contract.
- Run the "MetadataGeneration.py" script to create the metadata files.
- Host the metadata on the platform of you choice, the link needs to end with the number of the NFT or you need to change the contract.

## Solidity contract deployment
- Change your working directory to *node*
- Create a file called *.env* and fill it following this model:
```
API_POLYGON_URL = "Your API key"
PRIVATE_KEY = "Your polygon private key"
POLYGONSCAN_API_KEY = "Your polygonscan API key"
```
You can get an API key on [Alchemy](https://www.alchemy.com/), and if you want to verify your contract on [Polygonscan](https://polygonscan.com/) you need an API key for their site too.
- To compile the contracts run `npx hardhat compile` 
- To deploy the contracts open *scripts/deploy.js* and paste your baseURI (The link to your metadata) then run `npx hardhat run --network polygon ./scripts/deploy.js` 
- To mint the nfts open *scripts/mint.js*, paste your polygon public key and your contract adress then run `npx hardhat run --network polygon ./scripts/mint.js`.
- To verifiy your contract on Polygonscan run `npx hardhat verify --network polygon YOUR_CONTRACT_ADDRESS "0x58807baD0B376efc12F5AD86aAc70E78ed67deaE"` 

## Sell Orders Creation
- Run the "CreateSellOrders.py" python script to create all of the sell orders, you will have 15 seconds to type in your Metamask password when the firefox window appears. This will take ~6 seconds per NFT.

## To do

- Update the python scripts so it's easier to import other images and probabilites.