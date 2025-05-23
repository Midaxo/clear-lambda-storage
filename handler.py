"""
Lambda handler for clearing lambda storage.
"""

import os
from argparse import Namespace

from clear_lambda_storage import remove_old_lambda_versions


def clear_lambda_storage(_event, _context):
    """Lambda entry point."""
    regions = os.environ.get("REGIONS")
    enabled_regions = regions.split(",") if regions else None

    remove_old_lambda_versions(
        Namespace(
            token_key_id=None,
            token_secret=None,
            regions=enabled_regions,
            profile=None,
            num_to_keep=3,
            function_names=None,
            dry_run=None,
        )
    )
    return "Successful clean! 🗑 ✅"
