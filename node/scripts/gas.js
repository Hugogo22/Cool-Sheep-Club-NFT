const { ethers } = require("hardhat");

async function main() {
  console.log("\n----- START -----\n");

    const openSeaProxyAddress = "0x58807baD0B376efc12F5AD86aAc70E78ed67deaE";

    const CSC = await ethers.getContractFactory("CSC");
    const transac = CSC.getDeployTransaction(openSeaProxyAddress);
    console.log("Estimate gas: ", await ethers.provider.estimateGas(transac));

    console.log("\n----- END -----\n");
 }
 
 main()
   .then(() => process.exit(0))
   .catch(error => {
     console.error(error);
     process.exit(1);
   });