use crate::prelude::*;
use ktane_utils::edgework::Edgework;
use smallbitvec::SmallBitVec;
use std::collections::HashMap;
use std::sync::Arc;

mod starting;
mod timer;
pub use starting::cmd_run;
pub use timer::{Timer, TimerMode};

/// A key for the [`ShareMap`] in the [`Context`], refers to a mapping from [`ChannelId`]s to
/// [`Bomb`]s.
pub struct Bombs;

impl TypeMapKey for Bombs {
    type Value = HashMap<ChannelId, Arc<RwLock<Bomb>>>;
}

/// Helper function that, given a [`Context`] returns the [`Bomb`] for a given [`Message`]. If no
/// bomb is ticking in the message's channel, [`None`] is returned.
pub fn get_bomb(ctx: &Context, msg: &Message) -> Option<Arc<RwLock<Bomb>>> {
    ctx.data
        .read()
        .get::<Bombs>()
        .unwrap()
        .get(&msg.channel_id)
        .map(Arc::clone)
}

/// Helper function that, given a [`Context`] returns whether a bomb is ticking in the channel
/// corresponding to a [`Message`].
pub fn running_in(ctx: &Context, msg: &Message) -> bool {
    ctx.data
        .read()
        .get::<Bombs>()
        .unwrap()
        .contains_key(&msg.channel_id)
}

pub fn no_bomb() -> CommandResult {
    // TODO: link help
    Err((
        "No bomb in this channel".to_owned(),
        "No bomb is currently running in this channel. \
         Check out the help for more details."
            .to_owned(),
    ))
}

pub fn update_presence(ctx: &Context) {
    let bomb_count = ctx.data.read().get::<Bombs>().unwrap().len();
    let status = if bomb_count == 0 {
        OnlineStatus::Idle
    } else {
        OnlineStatus::Online
    };
    ctx.set_presence(
        Some(Activity::playing(&format!(
            "{} bomb{}. !help for help",
            bomb_count,
            if bomb_count == 1 { "" } else { "s" },
        ))),
        status,
    );
}

pub struct Bomb {
    pub edgework: Edgework,
    pub rule_seed: u32,
    pub timer: Timer,
    pub modules: Vec<Box<dyn Module>>,
    // This field is not public to prevent the temptation to just flip the relevant bit in the
    // module code when solved. Some bookkeeping is necessary, and as such the proper method of
    // registering a solve is TODO
    solve_state: SmallBitVec,
    pub channel: ChannelId,
    pub defusers: HashMap<UserId, Defuser>,
}

pub type ModuleNumber = u8;
pub const MAX_CLAIMS: usize = 3;
pub const MAX_MODULES: ModuleNumber = 101;

/// Stores information about a user that has interacted with the current bomb.
pub struct Defuser {
    pub last_view: Option<ModuleNumber>,
}

// TODO: Ack and stuff
pub fn cmd_detonate(ctx: &Context, msg: &Message, params: Parameters<'_>) -> CommandResult {
    if ctx
        .data
        .write()
        .get_mut::<Bombs>()
        .unwrap()
        .remove(&msg.channel_id)
        .is_none()
    {
        no_bomb()
    } else {
        update_presence(ctx);

        Ok(())
    }
}
