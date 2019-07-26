.PHONY: all
all: tools.stamp
	@true

tools.stamp: config/deps.py
	$(info doing [$@])
	@templar install_deps
	@make_helper touch-mkdir $@
