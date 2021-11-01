async function main() {
    console.log("\n----- START -----\n");

    //Paste your public key here
    const publicKey = '';

    //Paste your contract adress here
    const CSCadress = '';

    const CSC = await ethers.getContractFactory('CSC');
    const csc = await CSC.attach(CSCadress);

    for(let i = 0; i<99; i++){
      const rs = await csc.batchMintTo(100, publicKey);
      console.log(i, rs);
    }

    console.log("\n----- END -----\n");
 }
 
 main()
   .then(() => process.exit(0))
   .catch(error => {
     console.error(error);
     process.exit(1);
   });