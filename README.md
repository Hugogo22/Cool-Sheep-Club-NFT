# Cool-Sheep-Club-NFT

This repository has everything you need to make your own polygon ERC721 nfts. You only need python and node.js.
- The "Generation.py" python script will create the images and a txt file with the nft prices based on their rarity.
- The "MetadataGeneration.py" script will create the metadata files (There are two different scripts so you can have an ipfs link to the images)
- You can compile the contracts from the node directory with `npx hardhat compile`, deploy them with `npx hardhat run --network polygon ./scripts/deploy.js` and mint the nfts with `npx hardhat run --network polygon ./scripts/mint.js`.

## To do

- Update the python scripts so it's easier to import other images and probabilites.
- Update the node.js scripts with user inputs so you don't need to change the files manually.
- Add a script create a sell order for each nft.