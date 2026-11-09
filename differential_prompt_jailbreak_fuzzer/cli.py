"""CLI for differential-prompt-jailbreak-fuzzer."""
import sys
import argparse
from .fuzzer import PromptJailbreakFuzzer


def dummy_guardrail(prompt: str) -> bool:
    # Dummy guard: blocks if literal 'drop table' is present
    return "drop table" not in prompt.lower()


def main():
    parser = argparse.ArgumentParser(description="Differential Prompt Jailbreak Fuzzer CLI")
    parser.add_argument("--demo", action="store_true", help="Run differential jailbreak fuzzing demo")
    args = parser.parse_args()

    if args.demo:
        fuzzer = PromptJailbreakFuzzer()
        report = fuzzer.run_fuzz_test(["drop table users"], dummy_guardrail, mutations_per_payload=3)
        print(f"Fuzzing Complete: Total Tests = {report.total_mutations}")
        print(f"Robustness Score: {report.robustness_score:.1%}")
        print(f"Bypasses Found: {report.bypassed_count}")
        for b in report.successful_payloads:
            print(f"  -> {b}")
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
