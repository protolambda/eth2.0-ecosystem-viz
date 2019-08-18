graph = {
    # Clients
    'clients': {
        'yeeth': [
            'https://github.com/yeeth/BeaconChain.swift.git',
        ],
        'trinity': [
            'https://github.com/ethereum/trinity.git',
        ],
        'nimbus': [
            'https://github.com/status-im/nimbus.git',
            'https://github.com/status-im/nim-beacon-chain.git',
        ],
        'lighthouse': [
            'https://github.com/sigp/lighthouse.git',
        ],
        'prysm': [
            'https://github.com/prysmaticlabs/prysm.git',
        ],
        'lodestar': [
            'https://github.com/ChainSafe/lodestar.git',
        ],
        'artemis': [
            'https://github.com/PegaSysEng/artemis.git',
        ],
        'harmony': [
            'https://github.com/harmony-dev/beacon-chain-java.git',
        ],
        'shasper': [
            'https://github.com/paritytech/shasper.git',
        ],
    },

    'light-clients': {
        'quilt': [
            'https://github.com/lightclient/proof.git',
            'https://github.com/lightclient/single-pass-ssz-proof.git',
            'https://github.com/lightclient/simple-transfer.git',
        ]
    },

    'deposit_contract': {
        'vyper': [
            'https://github.com/ethereum/deposit_contract.git',
            ('deposit_contract', 'https://github.com/ethereum/eth2.0-specs.git', '/deposit_contract'),
        ],
        'runtimeverification': [
            ('verified_deposit_contract', 'https://github.com/runtimeverification/verified-smart-contracts.git', '/deposit/deposit')
        ],
    },

    'research': {
        'implementations': [
            'https://github.com/protolambda/lmd-ghost.git',
            'https://github.com/protolambda/eth2-shuffle.git',
            'https://github.com/CarlBeek/eth2.0-deposit-tooling.git',
            'https://github.com/CarlBeek/CBC_LMD.git',
        ],
        'papers': [
            ('lmd-ghost-casper-paper', 'https://git.overleaf.com/5c561e58be21326e99fdc90e')
        ]
    },

    'spec': {
        'exec': [
            ('pyspec', 'https://github.com/ethereum/eth2.0-specs.git', '/test_libs/pyspec'),
            ('ZRNT', 'https://github.com/protolambda/zrnt.git')
        ],
        'testgen': [
            ('eth2.0-spec-test-gen', 'https://github.com/ethereum/eth2.0-test-generators.git'),
            ('eth2.0-spec-test-gen', 'https://github.com/ethereum/eth2.0-specs.git', '/test_generators'),
        ],
        'spec': [
            ('specs', 'https://github.com/ethereum/eth2.0-specs.git', '/test_libs/spec')
        ]
    },

    'experiments': {
        'playgrounds': [
            'https://github.com/status-im/nimplay.git',
        ],
        'fork-choice': [
            'https://github.com/sigp/reduced_tree_fork_choice.git',

        ],
        'shuffling': [
            'https://github.com/sigp/shuffling_sandbox.git',
        ],
        'hacks': [
            'https://github.com/mkosowsk/Mytchmatic.git',
            'https://github.com/baconviewer/bacon-vision.git',
        ],
        'ideas': [
            'https://github.com/ethereum/firefly.git',
        ],
        'simulation': [
            'https://github.com/beacon-thugs-harmony/beacon_chain_simulator.git',
            'https://github.com/beacon-thugs-harmony/beacon_thugs_frontend.git',
            ('nim-browser-beaconchain', 'https://github.com/arnetheduck/arnetheduck.github.io.git', 'state_sim'),
        ],
    },

    'legacy': {
        'simulators': [
            'https://github.com/ethereum/simplecasper.git',
        ],
        'experimental': [
            'https://github.com/ethereum/sharding.git',
            'https://github.com/ethereum/beacon_chain.git',
        ]
    },

    'testing': {
        'configs': [
            ('spec-configs', 'https://github.com/ethereum/eth2.0-specs.git', '/configs')
        ],
        'spec-tests': [
            'https://github.com/ethereum/eth2.0-tests.git',
            'https://github.com/ethereum/eth2.0-spec-tests.git',
        ],
        'results': [
            'https://github.com/status-im/nim-eth2-testnet-data.git',
            'https://github.com/sigp/serenity-benches.git',
            'https://github.com/harmony-dev/eth2.0-benchmarks.git',
        ],
        'fuzzing': [
            'https://github.com/guidovranken/eth2.0-fuzzing.git',
        ],
        'services': [
            ('whiteblock-genesis', 'https://github.com/whiteblock/genesis.git'),
            ('whiteblock-cli', 'https://github.com/whiteblock/cli.git'),
            ('whiteblock-p2p-tests', 'https://github.com/whiteblock/p2p-tests.git'),
            ('antoine-tests', 'https://github.com/ethereum/eth2-client-tests.git'),
            ('ligthouse-setup', 'https://github.com/sigp/lighthouse-docker.git'),
        ],
        'monitoring': [
            'https://github.com/protolambda/eth2wtf-server.git',
            'https://github.com/protolambda/eth2wtf-client.git',
        ],
        'metrics': [
            'https://github.com/ethereum/eth2.0-metrics.git',
        ]
    },

    'networking': {
        'hobbits': {
            ('whiteblock-hobbits', 'https://github.com/whiteblock/hobbits.git'),
            ('lodestar-hobbits', 'https://github.com/ChainSafe/hobbits-ts.git'),
            ('yeeth-hobbits', 'https://github.com/yeeth/Hobbits.swift')
        },
        'libp2p': {
            'https://github.com/sigp/rust-libp2p.git',
            'https://github.com/libp2p/go-libp2p.git',
            'https://github.com/libp2p/js-libp2p.git',
            'https://github.com/libp2p/rust-libp2p',
            'https://github.com/libp2p/py-libp2p',
            'https://github.com/libp2p/jvm-libp2p',
        },
        'libp2p-daemons': {
            ('java-libp2p-daemon', 'https://github.com/jrhea/mothra.git'),
            'https://github.com/libp2p/go-libp2p-daemon.git',
            ('js-libp2p-deamon', 'https://github.com/libp2p/js-libp2p-daemon-client.git'),
        },
        'gossipsub': [
            'https://github.com/ChainSafe/gossipsub-js.git',
        ],
        'rpc': [
            'https://github.com/prysmaticlabs/ethereumapis.git',
            'https://github.com/prysmaticlabs/eth1-mock-rpc.git',
            'https://github.com/ethereum/eth2.0-apis.git',
        ]
    },

    'utils': {
        'ssz': [
            'https://github.com/prysmaticlabs/go-ssz.git',
            'https://github.com/protolambda/zssz.git',
            'https://github.com/ethereum/py-ssz.git',
            'https://github.com/ChainSafe/ssz-js.git',
            'https://github.com/yeeth/SimpleSerialize.swift.git',
        ],
        'bls': [
            'https://github.com/ChainSafe/bls-js.git',
            'https://github.com/prysmaticlabs/go-bls.git',
            'https://github.com/sigp/milagro_bls.git',
            'https://github.com/phoreproject/bls.git',
            'https://github.com/status-im/nim-blscurve.git',
            'https://github.com/ChainSafe/incubator-milagro-crypto-js.git',
            'https://github.com/rsgaetano/milagro-crypto-java.git',
            'https://github.com/ethereum/py_ecc.git',
            'https://github.com/Chia-Network/bls-signatures.git',
        ],
        'misc': [
            'https://github.com/ChainSafe/sha256-as.git',
            'https://github.com/prysmaticlabs/go-bitfield.git',
        ]
    },

    'education': {
        'websites': [
            'https://github.com/ChainSafe/simpleserialize.com.git',
        ],
        'resources': [
            'https://github.com/protolambda/eth2-docs.git',
            'https://github.com/protolambda/eth2-surround.git',
            'https://github.com/protolambda/beacon-schematic.git',
            'https://github.com/status-im/the-explainers.git',
            'https://github.com/sigp/eth2.0-resources.git',
        ],
    },

    'validators': {
        'clients': [
            ('yeeth-validator', 'https://github.com/yeeth/Pablo.swift.git'),
        ],
        # 'watchtowers': [],
    },

    'ewasm': {
        'integration': [
            ('quilt-scout', 'https://github.com/ewasm/scout.git'),
        ],
    },

    'project': {
        'management': [
            'https://github.com/sigp/lighthouse-pm.git',
            'https://github.com/ethereum/eth2.0-pm.git',
        ],
    },
}

import string

def url_to_out_name(repo_url):
    return ''.join(map(lambda x: x if (x in string.ascii_letters or x in string.digits) else '_', repo_url))
