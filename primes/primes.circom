pragma circom 2.0.0;


template PrimesFactorization() {
    signal input p;
    signal input q;
    signal input n;

    n === p * q;
}

component main {public [n]} = PrimesFactorization();