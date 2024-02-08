# Main network and testnet3 definitions

# Hellar src/chainparams.cpp
params = {
    'hellar_main': {
        'pubkey_address': 76, #L120
        'script_address': 16, #L122
        'genesis_hash': '00000fa67255a934520d6ff572828aa339af437d78ce6e6e6f4b2bd9ad30a0b9' #L110
    },
    'hellar_test': {
        'pubkey_address': 140, #L220
        'script_address': 19, #L222
        'genesis_hash': '00000b40bd778a9d4c0d35b674f7d09fec42e6c38bd3695e73a72b16519fcfe7' #L210
    }
}
