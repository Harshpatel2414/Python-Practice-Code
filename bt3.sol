pragma solidity ^0.8.7;

contract Bank{
    int balance;
    constructor() public{
        balance = 1000;
    }
    function showBalance() public view returns(int){
        return balance;
    } 
    function withdraw(int _money) public returns(int){
        balance = balance-_money;
        return balance;
    }

    function deposite(int _money) public returns(int){
        balance = balance+_money;
        return balance;
    }

}