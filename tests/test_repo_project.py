#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the repo_project module.
"""
import pytest

from repo_project import repo_project


def test_without_test_object():
    assert False


class TestRepo_project(object):
    @pytest.fixture
    def return_a_test_object(self):
        pass

    def test_repo_project(self, repo_project):
        assert False

    def test_with_error(self, repo_project):
        with pytest.raises(ValueError):
            pass
