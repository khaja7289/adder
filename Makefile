SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/..hdl/or.v
VERILOG_SOURCES += $(PWD)/wrappers/or_test.v
or:
         $(MAKE) sim MODULE=or_test TOPLEVEL=or_test
include $(shell cocotb-confing --makefiles)/Makefile.sim

