from edc_constants.constants import YES
from edc_metadata.constants import NOT_REQUIRED, REQUIRED

from edc_metadata_rules import CrfRule, register
from edc_metadata_rules import CrfRuleGroup
from edc_metadata_rules import P


app_label = 'trainee_subject'


@register()
class EducationQuestionnaireRuleGroup(CrfRuleGroup):

    work_status = CrfRule(
        predicate=P('work_status', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.communityquestionnaire'])

    class Meta:
        app_label = 'trainee_subject'
        source_model = f'{app_label}.educationquestionnaire'
