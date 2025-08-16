from udala.aktak import logger
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory


def vocab_term_title(context, name, termname):
    try:
        factory = getUtility(IVocabularyFactory, name)(context)
        termtitle = factory.getTerm(termname)
        return termtitle.title
    except Exception:
        logger.info("Vocabulary term not found: %s vocabulary: %s", termname, name)
        return ""
