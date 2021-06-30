# encoding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# Authentication for user filing issue (must have read/write access to repository to add issue to)
USERNAME = "changeme"
TOKEN = "changeme"

# The repository to add this issue to
REPO_OWNER = "changeme"
REPO_NAME = "changeme"

# Set new submission url of subject
NEW_SUB_URL = "https://arxiv.org/list/cs/new"

IMAGE_RETRIEVAL = [
    "image retrieval", "metric learning"
]
BACKBONE = [
    "vision transformer", "image transformer", "ViT"
]
VIDEO = [
    "video scene segmentation" "action recognition"
]
SSL = [
    "self-supervised"
]
MULTI_MODAL = [
    "multi modal", "multi-modal"
]
LARGE_SCALE = [
    "large-scale", "large scale"
]

# Keywords to search
KEYWORD_LIST = {
    "image-retrieval": IMAGE_RETRIEVAL,
    "video": VIDEO,
    "self-supervised learning": SSL,
    "multi-modal": MULTI_MODAL,
}
