# This file is part of curtin. See LICENSE file for copyright and license info.

from .releases import base_vm_classes as relbase
from .test_bcache_basic import TestBcacheBasic


class TestBcacheBug1718699(TestBcacheBasic):
    conf_file = "examples/tests/bcache-wipe-xfs.yaml"
    dirty_disks = False
    nr_cpus = 2
    extra_disks = ['10G']


class XenialTestBcacheBug1718699(relbase.xenial, TestBcacheBug1718699):
    __test__ = True


class BionicTestBcacheBug1718699(relbase.bionic, TestBcacheBug1718699):
    __test__ = True


class CosmicTestBcacheBug1718699(relbase.cosmic, TestBcacheBug1718699):
    __test__ = True


class DiscoTestBcacheBug1718699(relbase.disco, TestBcacheBug1718699):
    __test__ = True


class EoanTestBcacheBug1718699(relbase.eoan, TestBcacheBug1718699):
    __test__ = True

# vi: ts=4 expandtab syntax=python
