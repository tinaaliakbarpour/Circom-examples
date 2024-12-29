SHELL = zsh

circom = secretsharing.circom
r1cs = secretsharing.r1cs
wasm = secretsharing_js/secretsharing.wasm
wit_gen = secretsharing_js/generate_witness.js
compile_outputs = secretsharing_js/witness_calculator.js $(r1cs) $(wasm) $(wit_gen)
pk = secretsharing.pk
vk = secretsharing.vk
ptau = secretsharing.ptau
keys = $(pk) $(vk)
p_input = secretsharing.input.json
wit = secretsharing.wtns
wit_json = secretsharing.wtns.json
pf = secretsharing.pf.json
inst = secretsharing.inst.json
prove_outputs = $(pf) $(inst)

all: verify

$(compile_outputs): $(circom)
	circom $< --r1cs --wasm

$(ptau):
	snarkjs powersoftau new bn128 12 tmp.ptau
	snarkjs powersoftau prepare phase2 tmp.ptau $(ptau)
	rm tmp.ptau

$(keys): $(ptau) $(r1cs)
	snarkjs groth16 setup $(r1cs) $(ptau) $(pk)
	snarkjs zkey export verificationkey $(pk) $(vk)

$(wit): $(p_input) $(wasm) $(wit_gen)
	node $(wit_gen) $(wasm) $(p_input) $@

$(prove_outputs): $(wit) $(pk)
	snarkjs groth16 prove $(pk) $(wit) $(pf) $(inst)

.PHONY = verify clean

verify: $(pf) $(inst) $(vk)
	snarkjs groth16 verify $(vk) $(inst) $(pf)

clean:
	rm -f $(compile_outputs) $(ptau) $(keys) $(wit) $(prove_outputs) $(wit_json)
	rmdir secretsharing_js

info: 
	snarkjs wchk $(r1cs) $(wit)
	snarkjs wej $(wit) $(wit_json)
