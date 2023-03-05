module adder_test(
	input wire a,
	input wire b,
  input wire cin,
	output wire sum,
  output wire cout
);
full_adder dut(
	.a(a),
	.b(b),
	.cin(cin),
  .sum(sum),
  .cout(cout)
);

initial begin
	$dumpfile("full_adder.vcd");
	$dumpvars;
end
endmodule
