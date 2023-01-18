import logging
from stdpe.utils.logger import Logger


class TestLogger:

  # constants
  APP_INSIGHTS_KEY = "1632355d-fa45-431e-a7c9-2b1c6f5326d1"

  # class variables
  log = Logger()

  def test_create_logger(self):
    log_1 = Logger()
    log_2 = Logger()
    assert id(log_1) == id(log_2)

  def test_add_console_handler(self):
    self.log.add_console_handler(log_level=logging.INFO)
    self.log.add_console_handler(log_level=logging.INFO)
    nr_log_handlers = len(list(self.log.logger.handlers))
    assert nr_log_handlers == 1

  def test_set_console_level(self):
    self.log.set_console_log_level(level=logging.ERROR)
    for handler in self.log.logger.handlers:
      if handler.name == 'console':
        assert handler.level == logging.ERROR

  def test_add_az_handler(self):
    self.log.add_az_handler(log_level=logging.ERROR, app_insights_key=self.APP_INSIGHTS_KEY)
    self.log.add_az_handler(log_level=logging.ERROR, app_insights_key=self.APP_INSIGHTS_KEY)
    nr_log_handlers = len(list(self.log.logger.handlers))
    assert nr_log_handlers == 2

  def test_set_az_level(self):
    self.log.set_az_log_level(level=logging.INFO)
    for handler in self.log.logger.handlers:
      if handler.name == 'azure':
        assert handler.level == logging.INFO
