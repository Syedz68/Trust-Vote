# Trust Vote

This project is a straightforward decentralized application (dApp) that creates a simple election system using a smart contract written in Solidity. It lets users vote for their favorite party and see the vote status in real-time through a web interface. Users need to enter their name, an OTP (One Time Password) obtained from an Authorized Certificate Provider (this feature is not yet implemented, so for now, some random OTPs are pre-set in the system), and their voting choice. Once the OTP is verified, the vote will be counted.

## Features
- **Smart Contract**: Manages voting and keeps track of vote counts on the Ethereum blockchain.
- **Vote Casting**: Users can cast votes for different parties.
- **Real-Time Vote Status**: Displays current vote counts for each party.
- **Web Interface**: Flask-based application for user interaction.
- **Decentralized**: Ensures transparency and security by leveraging blockchain technology.

## Project Structures
- `Election.sol`: Contains the Solidity smart contract for the election.
- `trust_vote_deploy_o1.py`: Python script to compile the Solidity contract.
- `trust_vote_deploy_o2.py`: Python script to deploy and interact with the contract (placing votes, viewing status).
- `data.py`: Script to manage voter data using TinyDB.
- `app.py`: Flask web application to handle user interaction and display voting status.

## Prerequisites
- Python 3.6+
- pip (Python package installer)
- Solidity compiler (`solc`)
- Node.js and npm (for running a local blockchain, e.g., Ganache)

Below are images of the simulator:

