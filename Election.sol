// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract Election {
    uint public awlVoteCount;
    uint public bnpVoteCount;
    uint public neutral;
    uint totalVotes;

    function placeVote(uint vote) public {
        if(vote == 1) {
            awlVoteCount += 1;
            totalVotes += 1;
        }
        else if(vote == 2) {
            bnpVoteCount += 1;
            totalVotes += 1;
        }
        else {
            neutral += 1;
            totalVotes +=1;
        }
    }

    function viewVoteStatus() public view returns (uint, uint, uint, uint) {
        return (awlVoteCount, bnpVoteCount, neutral, totalVotes);
    }
}