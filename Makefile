SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/full_adder.v
VERILOG_SOURCES += $(PWD)/adder_test.v
adder:
         $(MAKE) sim MODULE=adder_test TOPLEVEL=adder_test
include $(shell cocotb-confing --makefiles)/Makefile.sim

