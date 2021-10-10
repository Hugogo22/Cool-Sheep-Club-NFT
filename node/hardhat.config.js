/**
 * @type import('hardhat/config').HardhatUserConfig
 */
require('dotenv').config();
require("@nomiclabs/hardhat-ethers");
require("@nomiclabs/hardhat-etherscan");
const { API_MUMBAI_URL, API_RINKEBY_URL, API_POLYGON_URL, PRIVATE_KEY, POLYGONSCAN_API_KEY } = process.env;
module.exports = {
   solidity: "0.8.0",
   defaultNetwork: "mumbai",
   networks: {
      hardhat: {},
      mumbai: {
         url: API_MUMBAI_URL,
         accounts: [`${PRIVATE_KEY}`]
      },
      polygon: {
         url: API_POLYGON_URL,
         accounts: [`${PRIVATE_KEY}`]
      },
      rinkeby: {
         url: API_RINKEBY_URL,
         accounts: [`${PRIVATE_KEY}`]
      }
   },
   etherscan: {
      apiKey: POLYGONSCAN_API_KEY  
   }
};
