# -*- makefile -*-
BUILD  := build
SOURCE := source
SYMBO  := symbolator
PARSER := parser
VERI   := verilog
VERIS  := verisphinx
TEST   := test

clean:
	-rm *~
	-rm -rf $(BUILD)/*
	-rm -rf $(BUILD)/.doctrees
	-rm  $(BUILD)/.buildinfo
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
	-rm $(VERIS)/*~
	-rm $(VERIS)/*.pyc
