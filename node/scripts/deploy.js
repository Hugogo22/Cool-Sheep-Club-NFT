async function main() {
    console.log("\n----- START -----\n");

    //const publicKey = "";
    const openSeaProxyAddress = "0x58807baD0B376efc12F5AD86aAc70E78ed67deaE";

    const CSC = await ethers.getContractFactory("CSC");
    console.log('Deploying CSC...');
 
    const csc = await CSC.deploy(openSeaProxyAddress);
    await csc.deployTransaction.wait();
    console.log("CSC deployed to address:", await csc.address);
    console.log("With name: %s ,and symbol: %s", await csc.name(), await csc.symbol());

    /*

    ---The commented lines parts deploy the factory, which cannot be used on polygon

    console.log("csc default admin role :", await csc.hasRole(csc.DEFAULT_ADMIN_ROLE(), publicKey));
    
    const cscAdminGrant = await csc.grantRole(csc.ADMIN_ROLE(), publicKey);
    await cscAdminGrant.wait();
    console.log("csc admin role :", await csc.hasRole(csc.ADMIN_ROLE(), publicKey));
    */

    // -----> Paste your baseURI here <-----
    let baseURI = "";
    const cscSetBaseURI = await csc.setBaseURI(baseURI);
    await cscSetBaseURI.wait();
    console.log("baseURI set");

    /*
    const CSCFactory = await ethers.getContractFactory("CSCFactory");
    console.log('Deploying CSCFactory...');

    const cscfactory = await CSCFactory.deploy(openSeaProxyAddress, csc.address);
    await cscfactory.deployTransaction.wait();
    console.log("CSCFactory deployed to address:", cscfactory.address);

    let factoryBaseURI = "ipfs://QmXKt7c8mM1vf3P9NvSJYntbqowEi2Z6VfwmSy8xBsXRT9/";
    const cscfactorySetBaseURI = await cscfactory.setBaseURI(factoryBaseURI);
    await cscfactorySetBaseURI.wait();
    console.log("factorybaseURI set");

    const cscMinterGrant = await csc.grantRole(csc.MINTER_ROLE(), cscfactory.address);
    await cscMinterGrant.wait();
    console.log("csc minter role :", await csc.hasRole(csc.MINTER_ROLE(), cscfactory.address));
    */

    console.log("\n----- END -----\n");
 }
 
 main()
   .then(() => process.exit(0))
   .catch(error => {
     console.error(error);
     process.exit(1);
   });