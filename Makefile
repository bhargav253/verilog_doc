# -*- makefile -*-
BUILD  := build
SOURCE := source
SYMBO  := symbolator
PARSER := parser
VERI   := verilog
TEST   := test

clean:
	-rm *~
	-rm -rf $(BUILD)/*
	-rm $(SOURCE)/*~
	-rm $(SYMBO)/*~
	-rm $(SYMBO)/*.pyc
	-rm $(PARSER)/*~
	-rm $(PARSER)/*.pyc
	-rm $(PARSER)/#*
	-rm $(TEST)/*~
	-rm $(TEST)/*.pyc
	-rm $(TEST)/#*
	-rm $(VERI)/*~
