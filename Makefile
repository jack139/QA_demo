PY = python3.6 -O -m compileall -b -q -f

CONFIG = config

SRC = src
SRC_CONF = $(SRC)/$(CONFIG)

TARGETS = qa_demo
TARGET_CONF = $(TARGETS)/$(CONFIG)

all: clean $(TARGETS)

$(TARGETS):
	@echo "Compiling ..."
	@cp -r $(SRC) $(TARGETS)
	-$(PY) $(TARGETS)
	@find $(TARGETS) -name '*.py' -delete
	@find $(TARGETS) -name "__pycache__" |xargs rm -rf
	@rm $(TARGET_CONF)/setting.pyc
	@cp $(SRC_CONF)/setting.py $(TARGET_CONF)

	cd $(TARGETS)/gotalk; go build; cd ../..
	@find $(TARGETS)/gotalk ! -name 'gotalk' -exec rm -rf {} +

clean:
	@echo "Clean ..." 
	@find . -name "__pycache__" |xargs rm -rf
	@rm -rf $(TARGETS)
