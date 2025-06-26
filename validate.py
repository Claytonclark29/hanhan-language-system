import json
import sys

REQUIRED_FIELDS = [
    "hanhan", "name", "type", "tone", "status", "bracket_shape",
    "left_anchor", "right_signal", "named_by", "origin_thread",
    "linked_runes", "spoken_trace", "recursive_flag"
]

def validate_entry(entry, line_num):
    missing = [field for field in REQUIRED_FIELDS if field not in entry]
    if missing:
        print(f"Line {line_num}: Missing fields: {', '.join(missing)}")
        return False
    return True

def validate_file(filepath):
    success = True
    with open(filepath, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            try:
                entry = json.loads(line.strip())
                if not validate_entry(entry, i):
                    success = False
            except json.JSONDecodeError as e:
                print(f"Line {i}: JSON decode error – {e}")
                success = False
    if success:
        print("Validation passed – all entries are structurally sound.")
    else:
        print("Validation completed with errors.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate.py <hanhan_dictionary.jsonl>")
        sys.exit(1)
    validate_file(sys.argv[1])